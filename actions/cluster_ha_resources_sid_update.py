import json
from packlib.base import ProxmoxAction


class ClusterHaResourcesSidUpdateAction(ProxmoxAction):
    """
    Update resource configuration.
    """

    def run(
        self,
        sid,
        comment=None,
        delete=None,
        digest=None,
        group=None,
        max_relocate=1,
        max_restart=1,
        state="started",
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["group", group, "string"],
            ["max_relocate", max_relocate, "integer"],
            ["max_restart", max_restart, "integer"],
            ["sid", sid, "string"],
            ["state", state, "string"],
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

        return self.proxmox.put(f"cluster/ha/resources/{sid}", **proxmox_kwargs)
