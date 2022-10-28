import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidMove_diskMoveVmDiskAction(ProxmoxAction):
    """
    Move volume to different storage or to a different VM.
    """

    def run(self, disk, node, vmid, bwlimit=move limit from datacenter or storage config, delete=False, digest=None, prox_format=None, storage=None, target_digest=None, target_disk=None, target_vmid=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "integer"],
            ["delete", delete, "boolean"],
            ["digest", digest, "string"],
            ["disk", disk, "string"],
            ["format", prox_format, "string"],
            ["node", node, "string"],
            ["storage", storage, "string"],
            ["target-digest", target_digest, "string"],
            ["target-disk", target_disk, "string"],
            ["target-vmid", target_vmid, "integer"],
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
            f"nodes/{node}/qemu/{vmid}/move_disk",
            **proxmox_kwargs
        )
        