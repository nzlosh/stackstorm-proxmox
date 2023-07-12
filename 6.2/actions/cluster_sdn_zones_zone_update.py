import json
from packlib.base import ProxmoxAction


class ClusterSdnZonesZoneUpdateAction(ProxmoxAction):
    """
    Update sdn zone object configuration.
    """

    def run(self, zone, bridge=None, controller=None, delete=None, digest=None, dp_id=None, mtu=None, nodes=None, peers=None, tag=None, vlan_protocol=None, vrf_vxlan=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bridge", bridge, "string"],
            ["controller", controller, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["dp-id", dp_id, "integer"],
            ["mtu", mtu, "integer"],
            ["nodes", nodes, "string"],
            ["peers", peers, "string"],
            ["tag", tag, "integer"],
            ["vlan-protocol", vlan_protocol, "string"],
            ["vrf-vxlan", vrf_vxlan, "integer"],
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
            f"cluster/sdn/zones/{zone}",
            **proxmox_kwargs
        )
        