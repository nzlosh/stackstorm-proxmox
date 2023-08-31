import json
from packlib.base import ProxmoxAction


class ClusterMappingUsbIdUpdateAction(ProxmoxAction):
    """
    Update a hardware mapping.
    """

    def run(self, prox_id, prox_map, delete=None, description=None, digest=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["delete", delete, "string"],
            ["description", description, "string"],
            ["digest", digest, "string"],
            ["id", prox_id, "string"],
            ["map", prox_map, "array"],
            
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

        return self.proxmox.put(
            f"cluster/mapping/usb/{id}",
            **proxmox_kwargs
        )
        