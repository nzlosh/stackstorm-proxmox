import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidMove_volumeAction(ProxmoxAction):
    """
    Move a rootfs-/mp-volume to a different storage
    """

    def run(
        self, node, storage, vmid, volume, bwlimit=0, delete=False, digest=None, profile_name=None
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "number"],
            ["delete", delete, "boolean"],
            ["digest", digest, "string"],
            ["node", node, "string"],
            ["storage", storage, "string"],
            ["vmid", vmid, "integer"],
            ["volume", volume, "string"],
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

        return self.proxmox.post(f"nodes/{node}/lxc/{vmid}/move_volume", **proxmox_kwargs)
