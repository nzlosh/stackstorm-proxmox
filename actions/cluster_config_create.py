import json
from packlib.base import ProxmoxAction


class ClusterConfigCreateAction(ProxmoxAction):
    """
    Generate new cluster configuration. If no links given, default to local IP address as link0.
    """

    def run(self, clustername, link_list=None, nodeid=None, votes=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["clustername", clustername, "string"],
            ["link[n]", link_list, "string"],
            ["nodeid", nodeid, "integer"],
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
            f"cluster/config",
            **proxmox_kwargs
        )
        