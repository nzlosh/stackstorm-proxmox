import json
from packlib.base import ProxmoxAction


class ClusterSdnVnetsVnetSubnetsSubnetUpdateAction(ProxmoxAction):
    """
    Update sdn subnet object configuration.
    """

    def run(
        self,
        subnet,
        delete=None,
        digest=None,
        dnszoneprefix=None,
        gateway=None,
        snat=None,
        vnet=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["dnszoneprefix", dnszoneprefix, "string"],
            ["gateway", gateway, "string"],
            ["snat", snat, "boolean"],
            ["subnet", subnet, "string"],
            ["vnet", vnet, "string"],
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

        return self.proxmox.put(f"cluster/sdn/vnets/{vnet}/subnets/{subnet}", **proxmox_kwargs)
