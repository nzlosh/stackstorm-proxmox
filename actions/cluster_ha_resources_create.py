import json
from packlib.base import ProxmoxAction


class ClusterHaResourcesCreateAction(ProxmoxAction):
    """
    Create a new HA resource.
    """

    def run(self, sid, comment=None, group=None, max_relocate=None, max_restart=None, state=None, prox_type=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["group", group, "string"],
            ["max_relocate", max_relocate, "integer"],
            ["max_restart", max_restart, "integer"],
            ["sid", sid, "string"],
            ["state", state, "string"],
            ["type", prox_type, "string"],
            
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
            f"cluster/ha/resources",
            **proxmox_kwargs
        )
        