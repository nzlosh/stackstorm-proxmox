import json
from packlib.base import ProxmoxAction


class NodesNodeDnsUpdateDnsAction(ProxmoxAction):
    """
    Write DNS settings.
    """

    def run(self, node, search, dns1=None, dns2=None, dns3=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["dns1", dns1, "string"],
            ["dns2", dns2, "string"],
            ["dns3", dns3, "string"],
            ["node", node, "string"],
            ["search", search, "string"],
        ]:
            if api_arg[1] is None:
                continue
            if "[n]" in api_arg[0]:
                unit_list = json.loads(api_arg[1])
                for i, v in enumerate(unit_list):
                    proxmox_kwargs[api_arg[0].replace("[n]", str(i))] = v
            else:
                if api_arg[2] == "boolean":
                    api_arg[1] = int(api_arg[1])
                proxmox_kwargs[api_arg[0]] = api_arg[1]

        return self.proxmox.put(f"nodes/{node}/dns", **proxmox_kwargs)
