import json
from packlib.base import ProxmoxAction


class ClusterConfigNodesNodeAddnodeAction(ProxmoxAction):
    """
    Adds a node to the cluster configuration. This call is for internal use.
    """

    def run(self, node, apiversion=None, force=None, link_list=None, new_node_ip=None, nodeid=None, votes=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["apiversion", apiversion, "integer"],
            ["force", force, "boolean"],
            ["link[n]", link_list, "string"],
            ["new_node_ip", new_node_ip, "string"],
            ["node", node, "string"],
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
            f"cluster/config/nodes/{node}",
            **proxmox_kwargs
        )
        