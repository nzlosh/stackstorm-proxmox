import json
from packlib.base import ProxmoxAction


class ClusterSdnVnetsVnetSubnetsCreateAction(ProxmoxAction):
    """
    Create a new sdn subnet object.
    """

    def run(self, subnet, prox_type, vnet, dnszoneprefix=None, gateway=None, snat=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["dnszoneprefix", dnszoneprefix, "string"],
            ["gateway", gateway, "string"],
            ["snat", snat, "boolean"],
            ["subnet", subnet, "string"],
            ["type", prox_type, "string"],
            ["vnet", vnet, "string"],
            
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
            f"cluster/sdn/vnets/{vnet}/subnets",
            **proxmox_kwargs
        )
        