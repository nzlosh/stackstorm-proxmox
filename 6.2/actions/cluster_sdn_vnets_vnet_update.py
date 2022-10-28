import json
from packlib.base import ProxmoxAction


class ClusterSdnVnetsVnetUpdateAction(ProxmoxAction):
    """
    Update sdn vnet object configuration.
    """

    def run(self, vnet, alias=None, delete=None, digest=None, ipv4=None, ipv6=None, mac=None, tag=None, vlanaware=None, zone=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["alias", alias, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["ipv4", ipv4, "string"],
            ["ipv6", ipv6, "string"],
            ["mac", mac, "string"],
            ["tag", tag, "integer"],
            ["vlanaware", vlanaware, "boolean"],
            ["vnet", vnet, "string"],
            ["zone", zone, "string"],
            
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
            f"cluster/sdn/vnets/{vnet}",
            **proxmox_kwargs
        )
        