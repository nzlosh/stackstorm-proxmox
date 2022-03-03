import json
from packlib.base import ProxmoxAction


class ClusterSdnZonesCreateAction(ProxmoxAction):
    """
    Create a new sdn zone object.
    """

    def run(
        self,
        prox_type,
        zone,
        bridge=None,
        controller=None,
        dns=None,
        dnszone=None,
        dp_id=None,
        exitnodes=None,
        ipam=None,
        mac=None,
        mtu=None,
        nodes=None,
        peers=None,
        reversedns=None,
        tag=None,
        vlan_protocol="802.1q",
        vrf_vxlan=None,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bridge", bridge, "string"],
            ["controller", controller, "string"],
            ["dns", dns, "string"],
            ["dnszone", dnszone, "string"],
            ["dp-id", dp_id, "integer"],
            ["exitnodes", exitnodes, "string"],
            ["ipam", ipam, "string"],
            ["mac", mac, "string"],
            ["mtu", mtu, "integer"],
            ["nodes", nodes, "string"],
            ["peers", peers, "string"],
            ["reversedns", reversedns, "string"],
            ["tag", tag, "integer"],
            ["type", prox_type, "string"],
            ["vlan-protocol", vlan_protocol, "string"],
            ["vrf-vxlan", vrf_vxlan, "integer"],
            ["zone", zone, "string"],
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

        return self.proxmox.post(f"cluster/sdn/zones", **proxmox_kwargs)
