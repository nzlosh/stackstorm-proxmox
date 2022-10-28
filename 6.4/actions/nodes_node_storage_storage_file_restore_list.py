import json
from packlib.base import ProxmoxAction


class NodesNodeStorageStorageFileRestoreListAction(ProxmoxAction):
    """
    List files and directories for single file restore under the given path.
    """

    def run(self, filepath, node, storage, volume, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["filepath", filepath, "string"],
            ["node", node, "string"],
            ["storage", storage, "string"],
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

        return self.proxmox.get(
            f"nodes/{node}/storage/{storage}/file-restore/list",
            **proxmox_kwargs
        )
        