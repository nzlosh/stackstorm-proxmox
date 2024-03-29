import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidSnapshotSnapnameDelsnapshotAction(ProxmoxAction):
    """
    Delete a VM snapshot.
    """

    def run(self, node, snapname, vmid, force=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["force", force, "boolean"],
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

        return self.proxmox.delete(
            f"nodes/{node}/qemu/{vmid}/snapshot/{snapname}",
            **proxmox_kwargs
        )
        