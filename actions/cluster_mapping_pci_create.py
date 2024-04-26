import json
from packlib.base import ProxmoxAction


class ClusterMappingPciCreateAction(ProxmoxAction):
    """
    Create a new hardware mapping.
    """

    def run(self, prox_id, prox_map, description=None, mdev=None, profile_name=None, api_timeout=5):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["description", description, "string"],
            ["id", prox_id, "string"],
            ["map", prox_map, "array"],
            ["mdev", mdev, "boolean"],
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

        return self.proxmox.post(f"cluster/mapping/pci", **proxmox_kwargs)
