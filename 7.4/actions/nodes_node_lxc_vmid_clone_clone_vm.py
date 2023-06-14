import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidCloneCloneVmAction(ProxmoxAction):
    """
    Create a container clone/copy
    """

    def run(self, newid, node, vmid, bwlimit=0, description=None, full=None, hostname=None, pool=None, snapname=None, storage=None, target=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "number"],
            ["description", description, "string"],
            ["full", full, "boolean"],
            ["hostname", hostname, "string"],
            ["newid", newid, "integer"],
            ["node", node, "string"],
            ["pool", pool, "string"],
            ["snapname", snapname, "string"],
            ["storage", storage, "string"],
            ["target", target, "string"],
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

        return self.proxmox.post(
            f"nodes/{node}/lxc/{vmid}/clone",
            **proxmox_kwargs
        )
        