import json
from packlib.base import ProxmoxAction


class ClusterConfigJoinAction(ProxmoxAction):
    """
    Joins this node into an existing cluster. If no links are given, default to IP resolved by node's hostname on single link (fallback fails for clusters with multiple links).
    """

    def run(self, fingerprint, hostname, password, force=None, link_list=None, nodeid=None, votes=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["fingerprint", fingerprint, "string"],
            ["force", force, "boolean"],
            ["hostname", hostname, "string"],
            ["link[n]", link_list, "string"],
            ["nodeid", nodeid, "integer"],
            ["password", password, "string"],
            ["votes", votes, "integer"],
            
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
            f"cluster/config/join",
            **proxmox_kwargs
        )
        