import json
from packlib.base import ProxmoxAction


class ClusterSdnControllersControllerUpdateAction(ProxmoxAction):
    """
    Update sdn controller object configuration.
    """

    def run(self, controller, asn=None, delete=None, digest=None, gateway_external_peers=None, gateway_nodes=None, peers=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["asn", asn, "integer"],
            ["controller", controller, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["gateway-external-peers", gateway_external_peers, "string"],
            ["gateway-nodes", gateway_nodes, "string"],
            ["peers", peers, "string"],
            
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
            f"cluster/sdn/controllers/{controller}",
            **proxmox_kwargs
        )
        