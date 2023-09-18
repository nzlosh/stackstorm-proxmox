import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidRemote_migrateRemoteMigrateVmAction(ProxmoxAction):
    """
    Migrate the container to another cluster. Creates a new migration task. EXPERIMENTAL feature!
    """

    def run(self, node, target_bridge, target_endpoint, target_storage, vmid, bwlimit=None, delete=None, online=None, restart=None, target_vmid=None, timeout=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "number"],
            ["delete", delete, "boolean"],
            ["node", node, "string"],
            ["online", online, "boolean"],
            ["restart", restart, "boolean"],
            ["target-bridge", target_bridge, "string"],
            ["target-endpoint", target_endpoint, "string"],
            ["target-storage", target_storage, "string"],
            ["target-vmid", target_vmid, "integer"],
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
            f"nodes/{node}/lxc/{vmid}/remote_migrate",
            **proxmox_kwargs
        )
        