#!/usr/bin/env python3
import argparse
import requests
import logging
import copy
import json
import re
import os

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

action_meta_jinja = r"""name: {{ action_name }}
pack: proxmox
runner_type: python-script
description: "{{ description }}"
enabled: true
entry_point: "{{ action_name }}.py"
{% if "properties" in parameters -%}
parameters:
{% for param, p in parameters.properties.items() -%}
  {{ "  " ~ p["st2_param"] }}:
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

action_jinja = r"""from lib.base import ProxmoxAction


class {{ class_name }}Action(ProxmoxAction):
    {{ '"'*3 }}
    {{ description }}
    {{ '"'*3 }}

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError

"""


def write_to_disk(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)


def cleanup_node(node):
    """
    Pre-rendering cleanup so the jinja template handles display and not data.
     - Escape special characters in descriptions.
     - Add python class name field
     - Add action name field
     - Add action parameter name field
     - Add python parameter name field
    """

    for (http_verb, method_meta) in node["info"].items():
        # Skip non http verb entries.
        if http_verb not in HTTP_METHODS:
            continue

        method_meta["action_name"] = action_name_from_node_path(node["path"], method_meta["name"])
        method_meta["class_name"] = class_name_from_nodepath(node["path"], method_meta["name"])

        for param, param_value in method_meta["parameters"].get("properties", {}).items():
            # Escape special characters
            if isinstance(param_value, dict) and "description" in param_value:
                method_meta["parameters"]["properties"][param]["description"] = json.dumps(
                    param_value["description"]
                )

            # Wrap default values of type string in quotes
            if "default" in param_value and param_value["type"] == "string":
                method_meta["parameters"]["properties"][param]["default"] = json.dumps(
                    param_value["default"]
                )

            # '-' is not a valid character for StackStorm action parameters.
            # [n] is stripped, but might need to create a way to communicate this through another parameter.
            method_meta["parameters"]["properties"][param]["st2_param"] = param.rsplit('[')[0].replace("-", "_")

            # mark certain fields as secret.
            if param in ["key", "password", "secret"]:
                method_meta["parameters"]["properties"][param]["st2_secret"] = "true"

        node["info"][http_verb] = method_meta

    return node


def write_st2_action(node, pack_path, lvl):
    """
    node: the proxmox spec to be processed
    lvl: present to respect function signature, but is unused.
    """
    action_path = "actions"
    if node["leaf"]:
        env = SandboxedEnvironment()
        template = env.from_string(action_jinja)

        clean_node = cleanup_node(copy.deepcopy(node))
        info = clean_node["info"]

        for (
            http_verb,
            method_object,
        ) in info.items():
            # Skip non http verb entries.
            if http_verb not in HTTP_METHODS:
                continue

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
                        "class_name": class_name,
                        "description": method_object["description"],
                        "parameters": method_object["parameters"],
                    }
                ),
            )


def class_name_from_nodepath(node_path, func_name):
    base_name = "".join(
        [n.capitalize() for n in node_path.lstrip("/").split("/") if not n.startswith("{")]
    )
    if base_name.endswith(func_name.capitalize()):
        class_name = base_name
    else:
        tmp = "".join([n.capitalize() for n in re.split(RE_SPLIT_FUNC_NAME, func_name)])
        class_name = f"{base_name}{tmp}"
    return class_name


def action_name_from_node_path(node_path, func_name):
    base_name = "_".join([n for n in node_path.lstrip("/").split("/") if not n.startswith("{")])
    if base_name.endswith(func_name):
        action_name = base_name
    else:
        action_name = f"{base_name}_{func_name}"
    return action_name


def write_st2_action_meta(node, pack_path, lvl):
    """
    node: the proxmox spec to be processed
    lvl: present to respect function signature, but is unused.
    """
    action_path = "actions"
    if node["leaf"]:
        env = SandboxedEnvironment()
        template = env.from_string(action_meta_jinja)

        clean_node = cleanup_node(copy.deepcopy(node))
        info = clean_node["info"]

        for (http_verb, method_object) in info.items():
            # Skip non http verb entries.
            if http_verb not in HTTP_METHODS:
                continue

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
    Extracts the jsonschema confounded inside the proxmox js documentation since a pure api
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
        data = read_from_http(source, username, password)
    else:
        data = read_from_disk(source)

    return extract_schema_from_js(data)


def walk_node(node, pack_path, lvl=0, funcs=[]):
    for fn in funcs:
        fn(node, pack_path, lvl)
    if "children" in node:
        lvl += 1
        for (_, v) in enumerate(node["children"]):
            walk_node(v, pack_path, lvl, funcs)


def generate_pack_content(source, pack_path, username=None, password=None, realm="pam"):
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

    schema = load_schema(source)
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
    generate_pack_content(args.api_source, args.pack_path, args.username, args.password, args.realm)
