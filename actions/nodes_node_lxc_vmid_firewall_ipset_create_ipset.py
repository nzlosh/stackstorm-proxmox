import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidFirewallIpsetCreateIpsetAction(ProxmoxAction):
    """
    Create new IPSet
    """

    def run(self, name, node, vmid, comment=None, digest=None, rename=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["digest", digest, "string"],
            ["name", name, "string"],
            ["node", node, "string"],
            ["rename", rename, "string"],
            ["vmid", vmid, "integer"],
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

        return self.proxmox.post(f"nodes/{node}/lxc/{vmid}/firewall/ipset", **proxmox_kwargs)
