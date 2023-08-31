import json
from packlib.base import ProxmoxAction


class ClusterSdnControllersCreateAction(ProxmoxAction):
    """
    Create a new sdn controller object.
    """

    def run(self, controller, prox_type, asn=None, bgp_multipath_as_path_relax=None, ebgp=None, ebgp_multihop=None, loopback=None, node=None, peers=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["asn", asn, "integer"],
            ["bgp-multipath-as-path-relax", bgp_multipath_as_path_relax, "boolean"],
            ["controller", controller, "string"],
            ["ebgp", ebgp, "boolean"],
            ["ebgp-multihop", ebgp_multihop, "integer"],
            ["loopback", loopback, "string"],
            ["node", node, "string"],
            ["peers", peers, "string"],
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
            f"cluster/sdn/controllers",
            **proxmox_kwargs
        )
        