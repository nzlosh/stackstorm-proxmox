#!/usr/bin/env python3
import argparse
import requests
import logging
import copy
import json
import re
import os

import pprint

import esprima

from jinja2.sandbox import SandboxedEnvironment
from urllib.parse import urlparse


log = logging.getLogger()

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

# Proxmox API documentation needs a few corrections so they're defined
# here in the format of a dictionary to override the library data.
PROXMOX_OVERRIDE = {
    "nodes_node_qemu_create_vm": {
        "bwlimit": {
            "default": 0,
        },
        "keyboard": {
            "default": "en-us",
        },
        "vcpus": {
            "default": "1",
        },
        "vmgenid": {
            "default": "1",
        },
    },
    "nodes_node_qemu_vmid_config_update_vm_async": {
        "keyboard": {
            "default": "en-us",
        },
        "vcpus": {
            "default": "1",
        },
        "vmgenid": {
            "default": "1",
        },
    },
    "nodes_node_qemu_vmid_config_update_vm": {
        "keyboard": {
            "default": "en-us",
        },
        "vcpus": {
            "default": "1",
        },
        "vmgenid": {
            "default": "1",
        },
    },
    "nodes_node_lxc_create_vm": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_lxc_vmid_clone_clone_vm": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_lxc_vmid_migrate_migrate_vm": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_lxc_vmid_move_volume": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_qemu_vmid_clone_clone_vm": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_qemu_vmid_migrate_migrate_vm": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_qemu_vmid_move_disk_move_vm_disk": {
        "bwlimit": {
            "default": 0,
        },
    },
    "nodes_node_qemu_vmid_status_start_vm_start": {
        "timeout": {
            "default": 10,
        },
    },
    "nodes_node_ceph_osd_createosd": {
        "wal_dev_size": {
            "default": 1,
        },
        "db_dev_size": {
            "default": 0.5,
        },
    },
    "access_users_userid_token_tokenid_update_token_info": {
        "expire": {
            "default": 1,
        },
    },
    "access_users_userid_token_tokenid_generate_token": {
        "expire": {
            "default": 1,
        },
    },
}


action_meta_jinja = r"""name: {{ action_name }}
pack: proxmox
runner_type: python-script
description: "{{ description }}"
enabled: true
entry_point: "{{ action_name }}.py"
{% if "properties" in parameters -%}
parameters:
{% for param, p in parameters.properties.items() -%}
  {{ "  " ~ p["safe_param"] }}:
    description: {{ p.description | default('"Description unavailable."') }}
    {% if "default" in p -%}
    default: {{ p.default }}
    {% endif -%}
    {% if "st2_secret" in p-%}
    secret: {{ p.st2_secret }}
    {% endif -%}
    {% if "enum" in p -%}
    enum:
    {% for i in p.enum -%}
    {{ "  - " ~ i }}
    {% endfor -%}
    {% endif -%}
    type: {{ p.type }}
    required: {{ (p.optional | default(0) == 0) | lower }}
{% endfor -%}
{% else %}
parameters: {}
{% endif %}
"""

action_jinja = r"""import json
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
{% set value = pp.get("default", "None") -%}
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
    {% set args = args + opts %}
    def run({{ args | join(", ") }}):
        super().run(profile_name)

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
    with open(filename, "w") as f:
        f.write(contents)


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

    for (http_verb, method_meta) in node["info"].items():
        # Skip non http verb entries.
        if http_verb not in HTTP_METHODS:
            log.debug(f"Skip unsupported http method {http_verb}.")
            continue

        # Translate "-" to be Python safe.
        method_meta["action_name"] = action_name_from_node_path(
            node["path"].replace("-", "/"), method_meta["name"].replace("-", "_")
        )
        method_meta["class_name"] = class_name_from_nodepath(
            node["path"].replace("-", "/"), method_meta["name"].replace("-", "_")
        )

        # Merge overrides to fix certain fields
        if method_meta["action_name"] in PROXMOX_OVERRIDE:
            for param in PROXMOX_OVERRIDE[method_meta["action_name"]]:
                method_meta["parameters"]["properties"][param].update(
                    PROXMOX_OVERRIDE[method_meta["action_name"]][param]
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

            # Wrap default values of type string in quotes
            if "default" in param_value and param_value["type"] == "string":
                method_meta["parameters"]["properties"][param]["default"] = json.dumps(
                    param_value["default"]
                )

            # Proxmox api defaults to integers for booleans types so we cast them for Python/StackStorm
            if "default" in param_value and param_value["type"] == "boolean":
                method_meta["parameters"]["properties"][param]["default"] = bool(
                    method_meta["parameters"]["properties"][param]["default"]
                )

            # [n] is transformed into a StackStorm array parameter using "format" to define the object.
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
        log.debug("{} {}".format(http_verb, node["path"]))

    return node


def write_st2_action(node, pack_path, lvl):
    """
    node: the proxmox spec to be processed
    lvl: present to respect function signature, but is unused.
    """
    action_path = "actions"

    env = SandboxedEnvironment()
    template = env.from_string(action_jinja)

    info = node["info"]

    for (http_verb, method_object) in info.items():

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
    base_name = "_".join([n for n in path.lstrip("/").split("/")])
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
    template = env.from_string(action_meta_jinja)

    info = node["info"]

    for (http_verb, method_object) in info.items():

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
    )

    prevention_token = resp.json()["data"]["CSRFPreventionToken"]
    ticket = resp.json()["data"]["ticket"]
    cookies = {"PVEAuthCookie": ticket}
    headers = {
        "CSRFPreventionToken": prevention_token,
    }

    # Get javascript document.
    resp = requests.get(
        f"{u.scheme}://{u.netloc}{u.path}{doc_path}", verify=False, headers=headers, cookies=cookies
    )

    return resp.text


def read_from_disk(filename):
    with open(filename, "r") as f:
        return "".join(f.readlines())


def extract_schema_from_js(data):
    """
    Extracts the jsonschema confounded inside the proxmox js documentation since a pure
    api specifications isn't officially provided.
    """
    tokens = esprima.parseScript(data, {"tokens": True}).tokens

    end = start = 0
    for (i, t) in enumerate(tokens):
        if t.value == "apiSchema" and tokens[i + 1].value == "=":
            start = i + 2
        if t.value == "]" and tokens[i + 1].value == ";":
            end = i + 1
            break
        if i > len(tokens) - 3:
            log.debug("Failed to find apiSchema")
            break

    return json.loads((" ".join([t.value for t in tokens[start:end]])))


def load_schema(source, username=None, password=None, realm=None):
    """
    source: url or filename to read the
    """
    if re.match(r"^https?://", source):
        data = read_from_http(source, username, password, realm)
    else:
        data = read_from_disk(source)

    return extract_schema_from_js(data)


def walk_node(node, pack_path, lvl=0, funcs=[]):
    if node.get("info", False):
        clean_node = cleanup_node(copy.deepcopy(node))
        for fn in funcs:
            fn(clean_node, pack_path, lvl)
    else:
        log.info("Skipping {} because it has no info.".format(node["path"]))
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

    DISPLAY = False
    if DISPLAY:
        generators.append(write_console)

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

    args = parser.parse_args()
    generate_pack_contents(
        args.api_source, args.pack_path, args.username, args.password, args.realm
    )
