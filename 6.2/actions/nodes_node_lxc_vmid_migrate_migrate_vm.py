import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidMigrateMigrateVmAction(ProxmoxAction):
    """
    Migrate the container to another node. Creates a new migration task.
    """

    def run(self, node, target, vmid, bwlimit=migrate limit from datacenter or storage config, force=None, online=None, restart=None, timeout=180, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "number"],
            ["force", force, "boolean"],
            ["node", node, "string"],
            ["online", online, "boolean"],
            ["restart", restart, "boolean"],
            ["target", target, "string"],
            ["timeout", timeout, "integer"],
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
            f"nodes/{node}/lxc/{vmid}/migrate",
            **proxmox_kwargs
        )
        