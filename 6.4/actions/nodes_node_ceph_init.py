import json
from packlib.base import ProxmoxAction


class NodesNodeCephInitAction(ProxmoxAction):
    """
    Create initial ceph default configuration and setup symlinks.
    """

    def run(self, node, cluster_network=None, disable_cephx=False, min_size=2, network=None, pg_bits=6, size=3, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["cluster-network", cluster_network, "string"],
            ["disable_cephx", disable_cephx, "boolean"],
            ["min_size", min_size, "integer"],
            ["network", network, "string"],
            ["node", node, "string"],
            ["pg_bits", pg_bits, "integer"],
            ["size", size, "integer"],
            
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
            f"nodes/{node}/ceph/init",
            **proxmox_kwargs
        )
        