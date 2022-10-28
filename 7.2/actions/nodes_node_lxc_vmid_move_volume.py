import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidMove_volumeAction(ProxmoxAction):
    """
    Move a rootfs-/mp-volume to a different storage or to a different container.
    """

    def run(self, node, vmid, volume, bwlimit=clone limit from datacenter or storage config, delete=False, digest=None, storage=None, target_digest=None, target_vmid=None, target_volume=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "number"],
            ["delete", delete, "boolean"],
            ["digest", digest, "string"],
            ["node", node, "string"],
            ["storage", storage, "string"],
            ["target-digest", target_digest, "string"],
            ["target-vmid", target_vmid, "integer"],
            ["target-volume", target_volume, "string"],
            ["vmid", vmid, "integer"],
            ["volume", volume, "string"],
            
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
            f"nodes/{node}/lxc/{vmid}/move_volume",
            **proxmox_kwargs
        )
        