import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidSnapshotSnapnameConfigUpdateSnapshotConfigAction(ProxmoxAction):
    """
    Update snapshot metadata.
    """

    def run(self, node, snapname, vmid, description=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["description", description, "string"],
            ["node", node, "string"],
            ["snapname", snapname, "string"],
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

        return self.proxmox.put(
            f"nodes/{node}/lxc/{vmid}/snapshot/{snapname}/config",
            **proxmox_kwargs
        )
        