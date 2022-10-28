import json
from packlib.base import ProxmoxAction


class ClusterHaGroupsGroupUpdateAction(ProxmoxAction):
    """
    Update ha group configuration.
    """

    def run(self, group, comment=None, delete=None, digest=None, nodes=None, nofailback=False, restricted=False, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["group", group, "string"],
            ["nodes", nodes, "string"],
            ["nofailback", nofailback, "boolean"],
            ["restricted", restricted, "boolean"],
            
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
            f"cluster/ha/groups/{group}",
            **proxmox_kwargs
        )
        