import json
from packlib.base import ProxmoxAction


class ClusterCephFlagsSetFlagsAction(ProxmoxAction):
    """
    Set/Unset multiple ceph flags at once.
    """

    def run(
        self,
        nobackfill=None,
        nodeep_scrub=None,
        nodown=None,
        noin=None,
        noout=None,
        norebalance=None,
        norecover=None,
        noscrub=None,
        notieragent=None,
        noup=None,
        pause=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["nobackfill", nobackfill, "boolean"],
            ["nodeep-scrub", nodeep_scrub, "boolean"],
            ["nodown", nodown, "boolean"],
            ["noin", noin, "boolean"],
            ["noout", noout, "boolean"],
            ["norebalance", norebalance, "boolean"],
            ["norecover", norecover, "boolean"],
            ["noscrub", noscrub, "boolean"],
            ["notieragent", notieragent, "boolean"],
            ["noup", noup, "boolean"],
            ["pause", pause, "boolean"],
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

        return self.proxmox.put(f"cluster/ceph/flags", **proxmox_kwargs)
