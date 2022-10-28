import json
from packlib.base import ProxmoxAction


class ClusterSdnZonesCreateAction(ProxmoxAction):
    """
    Create a new sdn zone object.
    """

    def run(self, prox_type, zone, advertise_subnets=None, bridge=None, bridge_disable_mac_learning=None, controller=None, disable_arp_nd_suppression=None, dns=None, dnszone=None, dp_id=None, exitnodes=None, exitnodes_local_routing=None, exitnodes_primary=None, ipam=None, mac=None, mtu=None, nodes=None, peers=None, reversedns=None, rt_import=None, tag=None, vlan_protocol="802.1q", vrf_vxlan=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["advertise-subnets", advertise_subnets, "boolean"],
            ["bridge", bridge, "string"],
            ["bridge-disable-mac-learning", bridge_disable_mac_learning, "boolean"],
            ["controller", controller, "string"],
            ["disable-arp-nd-suppression", disable_arp_nd_suppression, "boolean"],
            ["dns", dns, "string"],
            ["dnszone", dnszone, "string"],
            ["dp-id", dp_id, "integer"],
            ["exitnodes", exitnodes, "string"],
            ["exitnodes-local-routing", exitnodes_local_routing, "boolean"],
            ["exitnodes-primary", exitnodes_primary, "string"],
            ["ipam", ipam, "string"],
            ["mac", mac, "string"],
            ["mtu", mtu, "integer"],
            ["nodes", nodes, "string"],
            ["peers", peers, "string"],
            ["reversedns", reversedns, "string"],
            ["rt-import", rt_import, "string"],
            ["tag", tag, "integer"],
            ["type", prox_type, "string"],
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

        return self.proxmox.post(
            f"cluster/sdn/zones",
            **proxmox_kwargs
        )
        