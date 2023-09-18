import json
from packlib.base import ProxmoxAction


class NodesNodeConfigSetOptionsAction(ProxmoxAction):
    """
    Set node configuration options.
    """

    def run(self, node, acme=None, delete=None, description=None, digest=None, startall_onboot_delay=None, wakeonlan=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["acme", acme, "string"],
            ["delete", delete, "string"],
            ["description", description, "string"],
            ["digest", digest, "string"],
            ["node", node, "string"],
            ["startall-onboot-delay", startall_onboot_delay, "integer"],
            ["wakeonlan", wakeonlan, "string"],
            
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

        return self.proxmox.put(
            f"nodes/{node}/config",
            **proxmox_kwargs
        )
        