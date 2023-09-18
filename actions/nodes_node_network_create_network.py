import json
from packlib.base import ProxmoxAction


class NodesNodeNetworkCreateNetworkAction(ProxmoxAction):
    """
    Create network device configuration
    """

    def run(self, iface, node, prox_type, address=None, address6=None, autostart=None, bond_mode=None, bond_xmit_hash_policy=None, bridge_ports=None, bridge_vlan_aware=None, cidr=None, cidr6=None, comments=None, comments6=None, gateway=None, gateway6=None, netmask=None, netmask6=None, ovs_bonds=None, ovs_bridge=None, ovs_options=None, ovs_ports=None, ovs_tag=None, slaves=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["address", address, "string"],
            ["address6", address6, "string"],
            ["autostart", autostart, "boolean"],
            ["bond_mode", bond_mode, "string"],
            ["bond_xmit_hash_policy", bond_xmit_hash_policy, "string"],
            ["bridge_ports", bridge_ports, "string"],
            ["bridge_vlan_aware", bridge_vlan_aware, "boolean"],
            ["cidr", cidr, "string"],
            ["cidr6", cidr6, "string"],
            ["comments", comments, "string"],
            ["comments6", comments6, "string"],
            ["gateway", gateway, "string"],
            ["gateway6", gateway6, "string"],
            ["iface", iface, "string"],
            ["netmask", netmask, "string"],
            ["netmask6", netmask6, "integer"],
            ["node", node, "string"],
            ["ovs_bonds", ovs_bonds, "string"],
            ["ovs_bridge", ovs_bridge, "string"],
            ["ovs_options", ovs_options, "string"],
            ["ovs_ports", ovs_ports, "string"],
            ["ovs_tag", ovs_tag, "integer"],
            ["slaves", slaves, "string"],
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
            f"nodes/{node}/network",
            **proxmox_kwargs
        )
        