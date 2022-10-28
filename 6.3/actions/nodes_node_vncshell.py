import json
from packlib.base import ProxmoxAction


class NodesNodeVncshellAction(ProxmoxAction):
    """
    Creates a VNC Shell proxy.
    """

    def run(self, node, cmd="login", cmd_opts="", height=None, upgrade=False, websocket=None, width=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["cmd", cmd, "string"],
            ["cmd-opts", cmd_opts, "string"],
            ["height", height, "integer"],
            ["node", node, "string"],
            ["upgrade", upgrade, "boolean"],
            ["websocket", websocket, "boolean"],
            ["width", width, "integer"],
            
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

        return self.proxmox.post(
            f"nodes/{node}/vncshell",
            **proxmox_kwargs
        )
        