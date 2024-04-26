import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidMigrateMigrateVmAction(ProxmoxAction):
    """
    Migrate virtual machine. Creates a new migration task.
    """

    def run(
        self,
        node,
        target,
        vmid,
        bwlimit=None,
        force=None,
        migration_network=None,
        migration_type=None,
        online=None,
        targetstorage=None,
        with_local_disks=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "integer"],
            ["force", force, "boolean"],
            ["migration_network", migration_network, "string"],
            ["migration_type", migration_type, "string"],
            ["node", node, "string"],
            ["online", online, "boolean"],
            ["target", target, "string"],
            ["targetstorage", targetstorage, "string"],
            ["vmid", vmid, "integer"],
            ["with-local-disks", with_local_disks, "boolean"],
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

        return self.proxmox.post(f"nodes/{node}/qemu/{vmid}/migrate", **proxmox_kwargs)
