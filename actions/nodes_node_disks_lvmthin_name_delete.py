import json
from packlib.base import ProxmoxAction


class NodesNodeDisksLvmthinNameDeleteAction(ProxmoxAction):
    """
    Remove an LVM thin pool.
    """

    def run(self, name, node, volume_group, cleanup_config=None, cleanup_disks=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["cleanup-config", cleanup_config, "boolean"],
            ["cleanup-disks", cleanup_disks, "boolean"],
            ["name", name, "string"],
            ["node", node, "string"],
            ["volume-group", volume_group, "string"],
            
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
            f"nodes/{node}/disks/lvmthin/{name}",
            **proxmox_kwargs
        )
        