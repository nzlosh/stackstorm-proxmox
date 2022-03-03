import json
from packlib.base import ProxmoxAction


class NodesNodeStorageStoragePrunebackupsDeleteAction(ProxmoxAction):
    """
    Prune backups. Only those using the standard naming scheme are considered.
    """

    def run(self, node, storage, prune_backups=None, prox_type=None, vmid=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["node", node, "string"],
            ["prune-backups", prune_backups, "string"],
            ["storage", storage, "string"],
            ["type", prox_type, "string"],
            ["vmid", vmid, "integer"],
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

        return self.proxmox.delete(f"nodes/{node}/storage/{storage}/prunebackups", **proxmox_kwargs)
