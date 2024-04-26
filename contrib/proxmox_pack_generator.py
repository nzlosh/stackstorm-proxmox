#!/usr/bin/env python3
import argparse
import copy
import json
import logging
import os
import pathlib
import re
import shutil
import sys
from urllib.parse import urlparse

import esprima
import requests
from jinja2.sandbox import SandboxedEnvironment

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

console_log = logging.StreamHandler()
console_log.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
console_log.setFormatter(formatter)

log.addHandler(console_log)

RE_SPLIT_FUNC_NAME = re.compile(r"-|_")
HTTP_METHODS = [
    "PUT",
    "GET",
    "POST",
    "DELETE",
]

# The proxmox api uses arguments that conflict with Python built-in and
# reserve words so they're here to detect and render proxmox arguments
# to be python safe.
PYTHON_BUILTIN = [
    "abs",
    "aiter",
    "all",
    "any",
    "anext",
    "ascii",
    "bin",
    "bool",
    "breakpoint",
    "bytearray",
    "bytes",
    "callable",
    "chr",
    "classmethod",
    "compile",
    "complex",
    "delattr",
    "dict",
    "dir",
    "divmod",
    "enumerate",
    "eval",
    "exec",
    "filter",
    "float",
    "format",
    "frozenset",
    "getattr",
    "globals",
    "hasattr",
    "hash",
    "help",
    "hex",
    "id",
    "input",
    "int",
    "isinstance",
    "issubclass",
    "iter",
    "len",
    "list",
    "locals",
    "map",
    "max",
    "memoryview",
    "min",
    "next",
    "object",
    "oct",
    "open",
    "ord",
    "pow",
    "print",
    "property",
    "range",
    "repr",
    "reversed",
    "round",
    "set",
    "setattr",
    "slice",
    "sorted",
    "staticmethod",
    "str",
    "sum",
    "super",
    "tuple",
    "type",
    "vars",
    "zip",
]

PYTHON_KEYWORDS = [
    "False",
    "def",
    "if",
    "raise",
    "None",
    "del",
    "import",
    "return",
    "True",
    "elif",
    "in",
    "try",
    "and",
    "else",
    "is",
    "while",
    "as",
    "except",
    "lambda",
    "with",
    "assert",
    "finally",
    "nonlocal",
    "yield",
    "break",
    "for",
    "not",
    "class",
    "from",
    "or",
    "continue",
    "global",
    "pass",
]


ACTION_META_JINJA = r"""name: {{ action_name }}
pack: proxmox
runner_type: python-script
description: "{{ description }}"
enabled: true
entry_point: "{{ action_name }}.py"
{% if "properties" in parameters -%}
parameters:
  api_timeout:
    description: "Time in seconds to wait for API response. (Default: 5)"
    type: integer
    required: false
    default: 5
{% for param, p in parameters.properties.items() -%}
  {{ "  " ~ p["safe_param"] }}:
    description: {{ p.description | default('"Description unavailable."') }}
    {% if "st2_secret" in p-%}
    secret: {{ p.st2_secret }}
    {% endif -%}
    type: {{ p.type }}
    required: {{ (p.optional | default(0) == 0) | lower }}
{% endfor -%}
{% else %}
parameters: {}
{% endif %}
"""

ACTION_JINJA = r"""import json
from packlib.base import ProxmoxAction


class {{ class_name }}Action(ProxmoxAction):
    {{ '"'*3 }}
    {{ description }}
    {{ '"'*3 }}
{% set opts = [] -%}
{% set args = ["self"] -%}
{% set api_args = {} -%}

{% for p in parameters.properties -%}
{% set pp = parameters.properties[p] -%}
{% if "optional" in pp and pp.optional == 1 -%}
{% set value = "None" -%}
{% set _ = opts.append(pp.safe_param ~ "=" ~ value) -%}
{% if "{" ~ p ~ "}" not in parameters.path and p not in ["profile_name"] -%}
{% set _ = api_args.update({p: pp.safe_param}) -%}
{% endif -%}
{% else -%}
{% set _ = args.append(pp.safe_param) -%}
{% if "{" ~ p ~ "}" not in parameters.path and p not in ["profile_name"] -%}
{% set _ = api_args.update({p: pp.safe_param}) -%}
{% endif -%}
{% endif -%}
{% endfor -%}
    {% set args = args + opts + ["api_timeout=5"] %}
    def run({{ args | join(", ") }}):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        {% if api_args -%}
        for api_arg in [
            {% for k, v in api_args.items() -%}
            ["{{ k }}", {{ v }}, "{{ parameters.properties[k]["type"] }}"],
            {% endfor %}
        ]:
            if api_arg[1] is None:
                continue
            if '[n]' in api_arg[0]:
                unit_list = json.loads(api_arg[1])
                for i, v in enumerate(unit_list):
                    proxmox_kwargs[api_arg[0].replace("[n]", str(i))] = v
            else:
                if api_arg[2] == "boolean":
                    api_arg[1] = int(api_arg[1])
                proxmox_kwargs[api_arg[0]] = api_arg[1]

        return self.proxmox.{{ http_verb.lower() }}(
            f"{{ path.lstrip("/") }}",
            **proxmox_kwargs
        )
        {% else -%}
        return self.proxmox.{{ http_verb.lower() }}(f"{{ path.lstrip("/") }}")
        {% endif -%}
"""


def write_to_disk(filename, contents):
    with open(filename, "w", encoding="utf-8") as fhandle:
        fhandle.write(contents)


def cleanup_node(node):
    """
    Pre-rendering cleanup so the jinja template handles display and not data processing.
     - Escape special characters in descriptions.
     - Add python class name field
     - Add action name field
     - Add action parameter name field
     - Insert StackStorm pack parameters. e.g. profile_name action parameter
     - Add python parameter name field
    """

    for http_verb, method_meta in node["info"].items():
        # Skip non http verb entries.
        if http_verb not in HTTP_METHODS:
            log.debug("Skip unsupported http method %s.", http_verb)
            continue

        # Translate "-" to be Python safe.
        method_meta["action_name"] = action_name_from_node_path(
            node["path"].replace("-", "/"), method_meta["name"].replace("-", "_")
        )
        method_meta["class_name"] = class_name_from_nodepath(
            node["path"].replace("-", "/"), method_meta["name"].replace("-", "_")
        )

        if "properties" not in method_meta["parameters"]:
            method_meta["parameters"]["properties"] = {}

        # Additional StackStorm parameters inserted here.
        method_meta["parameters"]["properties"]["profile_name"] = {
            "type": "string",
            "description": "The profile to use to run the action.",
            "optional": 1,
        }

        for param, param_value in method_meta["parameters"]["properties"].items():
            # Escape special characters and remove formatting from descriptions.
            if isinstance(param_value, dict) and "description" in param_value:
                method_meta["parameters"]["properties"][param]["description"] = json.dumps(
                    param_value["description"].replace("\n", " ").replace("\t", "")
                )

            # [n] is transformed into a StackStorm array parameter using
            # "format" to define the object.
            if "[n]" in param:
                method_meta["parameters"]["properties"][param]["safe_param"] = param.replace(
                    "[n]", "_list"
                )
            else:
                # '-' is not a valid character for StackStorm action parameters.
                method_meta["parameters"]["properties"][param]["safe_param"] = param.replace(
                    "-", "_"
                )

            # rename any variables that conflict with Python built-in or reserve words
            if param in PYTHON_KEYWORDS + PYTHON_BUILTIN:
                method_meta["parameters"]["properties"][param]["safe_param"] = (
                    "prox_" + method_meta["parameters"]["properties"][param]["safe_param"]
                )

            # mark certain fields as secret.
            if param in ["key", "password", "secret"]:
                method_meta["parameters"]["properties"][param]["st2_secret"] = "true"

        node["info"][http_verb] = method_meta
        log.debug("%s %s", http_verb, node["path"])

    return node


def write_st2_action(node, pack_path, lvl):
    """
    node: the proxmox spec to be processed
    pack_path: the path to the pack being generated.
    lvl: present to respect function signature, but is unused.
    """
    action_path = "actions"

    env = SandboxedEnvironment()
    template = env.from_string(ACTION_JINJA)

    info = node["info"]

    for http_verb, method_object in info.items():
        action_name = info[http_verb]["action_name"]
        class_name = info[http_verb]["class_name"]
        filename = os.path.join(
            pack_path,
            action_path,
            f"{action_name}.py",
        )

        write_to_disk(
            filename,
            template.render(
                {
                    "http_verb": http_verb,
                    "class_name": class_name,
                    "description": method_object["description"],
                    "parameters": method_object["parameters"],
                    "path": node["path"],
                }
            ),
        )


def class_name_from_nodepath(node_path, method_name):
    # strip out { and } making variables plain text to ensure unique class names.
    path = node_path.replace("{", "").replace("}", "")
    base_name = "".join([n.capitalize() for n in path.lstrip("/").split("/")])
    if base_name.endswith(method_name.capitalize()):
        class_name = base_name
    else:
        tmp = "".join([n.capitalize() for n in re.split(RE_SPLIT_FUNC_NAME, method_name)])
        class_name = f"{base_name}{tmp}"
    return class_name


def action_name_from_node_path(node_path, method_name):
    # strip out { and } making variables plain text.
    path = node_path.replace("{", "").replace("}", "")
    base_name = "_".join(path.lstrip("/").split("/"))
    if base_name.endswith(method_name):
        action_name = base_name
    else:
        action_name = f"{base_name}_{method_name}"

    return action_name


def write_st2_action_meta(node, pack_path, lvl):
    """
    node: the proxmox spec to be processed
    lvl: present to respect function signature, but is unused.
    """
    action_path = "actions"

    env = SandboxedEnvironment()
    template = env.from_string(ACTION_META_JINJA)

    info = node["info"]

    for http_verb, method_object in info.items():
        action_name = info[http_verb]["action_name"]
        filename = os.path.join(pack_path, action_path, f"{action_name}.yaml")

        write_to_disk(
            filename,
            template.render(
                {
                    "action_name": action_name,
                    "description": method_object["description"],
                    "parameters": method_object["parameters"],
                }
            ),
        )


def write_console(node, pack_path, lvl):
    ident = "   " * lvl
    if "text" in node:
        print(f"{ident}{node['text']}")
    else:
        print(f"{ident}{type(node)}")

    if "path" in node:
        print(node["path"])

    if "info" in node:
        for k in node["info"]:
            print(f"[{k}]: ")
            for kk in node["info"][k]:
                print(f"{kk}: {node['info'][k][kk]}")


def read_from_http(url, username, password, realm):
    u = urlparse(url)
    auth_path = "/api2/extjs/access/ticket"
    doc_path = "/pve-docs/api-viewer/apidoc.js"
    if u.path.endswith("/"):
        auth_path = auth_path.lstrip("/")
        doc_path = doc_path.lstrip("/")

    # Get a ticket
    resp = requests.post(
        f"{u.scheme}://{u.netloc}{u.path}{auth_path}",
        verify=False,
        data={
            "username": username,
            "password": password,
            "realm": realm,
        },
        timeout=20,
    )

    prevention_token = resp.json()["data"]["CSRFPreventionToken"]
    ticket = resp.json()["data"]["ticket"]
    cookies = {"PVEAuthCookie": ticket}
    headers = {
        "CSRFPreventionToken": prevention_token,
    }

    # Get javascript document.
    resp = requests.get(
        f"{u.scheme}://{u.netloc}{u.path}{doc_path}",
        verify=False,
        headers=headers,
        cookies=cookies,
        timeout=20,
    )

    return resp.text


def read_from_disk(filename):
    with open(filename, "r", encoding="utf-8") as fhandle:
        return "".join(fhandle.readlines())


def copy_packlib(pack_path):
    """
    Given the pack root directory, the contrib and actions directories
    are extrapolated as the source/destination to copy python modules.
    """
    action_path = pathlib.Path(pack_path)
    action_path = action_path.joinpath("actions").resolve()
    if not action_path.exists():
        print(f"Abort: 'actions' path not found at {action_path}.")
        sys.exit(1)
    # Create the directory packlib inside the actions directory.
    packlib_dst = action_path.joinpath("packlib")
    if not packlib_dst.exists():
        try:
            os.mkdir(packlib_dst)
        except FileExistsError as ignored:
            pass

    # Copy the contents of the packlib directory from the contrib directory.
    packlib_src = pathlib.Path(pack_path)
    packlib_src = packlib_src.joinpath("contrib/packlib")
    if not packlib_src.exists():
        print(f"Abort: 'packlib' path not found at {packlib_path}")
        sys.exit(1)

    shutil.copytree(packlib_src, packlib_dst, dirs_exist_ok=True)


def extract_schema_from_js(data):
    """
    Extracts the jsonschema confounded inside the proxmox js documentation since a pure
    api specifications isn't officially provided.
    """
    data = data.replace("?.", ".")
    tokens = esprima.parseScript(data, {"tokens": True}).tokens

    v6x_token = "pveapi"
    v72_token = "apiSchema"

    end = start = 0
    for i, t in enumerate(tokens):
        if t.value in [v6x_token, v72_token] and tokens[i + 1].value == "=":
            log.debug("API schema variable start found!")
            start = i + 2
        if t.value == "]" and tokens[i + 1].value == ";":
            end = i + 1
            log.debug("API schema variable end found!")
            break
        if i > len(tokens) - 3:
            log.debug("Failed to find the API schema variable")
            break

    s = ""
    for i in range(start, end):
        s += tokens[i].value.strip()

    return json.loads(s)


def load_schema(source, username=None, password=None, realm=None):
    """
    source: url or filename to read the
    """
    if re.match(r"^https?://", source):
        data = read_from_http(source, username, password, realm)
    else:
        data = read_from_disk(source)

    return extract_schema_from_js(data)


def walk_node(node, pack_path, lvl=0, funcs=None):
    if funcs is None:
        funcs = []
    if node.get("info", False):
        clean_node = cleanup_node(copy.deepcopy(node))
        for fn in funcs:
            fn(clean_node, pack_path, lvl)
    else:
        log.info("Skipping %s because it has no info.", node["path"])
    if "children" in node:
        lvl += 1
        for v in node["children"]:
            walk_node(v, pack_path, lvl, funcs)


def generate_pack_contents(source, pack_path, username=None, password=None, realm="pam"):
    """
    Input:
      source: Proxmox API url to authenticate and download the javascript document or a filesystem
              path to read the javascript api document from.
      pack_path: Path to pack into which content will be written.
      username: username for Proxmox API.
      password: password for Proxmox API.
      realm: authentication realm to validate credentials for Proxmox API.
    """
    generators = [write_st2_action_meta, write_st2_action]

    # Uncomment when you want to see console output
    # generators.append(write_console)

    schema = load_schema(source, username, password, realm)
    for i in schema:
        log.debug(i.keys())
        walk_node(i, pack_path, 0, generators)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proxmox pack action generator.")
    parser.add_argument(
        "api_source",
        type=str,
        help="Source of API documentation.  Can be filename or url to apidoc.",
    )
    parser.add_argument(
        "--username",
        type=str,
        dest="username",
        default=None,
        help="Proxmox API username",
    )
    parser.add_argument(
        "--password",
        type=str,
        dest="password",
        default=None,
        help="Proxmox API password",
    )
    parser.add_argument(
        "--realm",
        type=str,
        dest="realm",
        default="pam",
        help="Proxmox API authentication realm",
    )
    parser.add_argument(
        "--pack_path",
        type=str,
        required=True,
        dest="pack_path",
        help="Path to pack where files will be written.",
    )
    parser.add_argument(
        "--overrides",
        type=str,
        required=False,
        dest="overrides",
        help="Filename for overrides in JSON format.",
    )

    args = parser.parse_args()
    generate_pack_contents(
        args.api_source, args.pack_path, args.username, args.password, args.realm
    )
    copy_packlib(args.pack_path)
