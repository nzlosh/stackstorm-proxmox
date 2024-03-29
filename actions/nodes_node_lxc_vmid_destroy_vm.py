import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidDestroyVmAction(ProxmoxAction):
    """
    Destroy the container (also delete all uses files).
    """

    def run(self, node, vmid, destroy_unreferenced_disks=None, force=None, purge=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["destroy-unreferenced-disks", destroy_unreferenced_disks, "boolean"],
            ["force", force, "boolean"],
            ["node", node, "string"],
            ["purge", purge, "boolean"],
            ["vmid", vmid, "integer"],
            
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

        return self.proxmox.delete(
            f"nodes/{node}/lxc/{vmid}",
            **proxmox_kwargs
        )
        