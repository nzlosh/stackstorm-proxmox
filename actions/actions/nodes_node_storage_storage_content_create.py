import json
from packlib.base import ProxmoxAction


class NodesNodeStorageStorageContentCreateAction(ProxmoxAction):
    """
    Allocate disk images.
    """

    def run(self, filename, node, size, storage, vmid, prox_format=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["filename", filename, "string"],
            ["format", prox_format, "string"],
            ["node", node, "string"],
            ["size", size, "string"],
            ["storage", storage, "string"],
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
            f"nodes/{node}/storage/{storage}/content",
            **proxmox_kwargs
        )
        