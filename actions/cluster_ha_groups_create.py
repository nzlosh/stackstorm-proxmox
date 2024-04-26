import json
from packlib.base import ProxmoxAction


class ClusterHaGroupsCreateAction(ProxmoxAction):
    """
    Create a new HA group.
    """

    def run(
        self,
        group,
        nodes,
        comment=None,
        nofailback=None,
        restricted=None,
        prox_type=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["group", group, "string"],
            ["nodes", nodes, "string"],
            ["nofailback", nofailback, "boolean"],
            ["restricted", restricted, "boolean"],
            ["type", prox_type, "string"],
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

        return self.proxmox.post(f"cluster/ha/groups", **proxmox_kwargs)
