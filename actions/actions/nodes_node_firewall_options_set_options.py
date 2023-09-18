import json
from packlib.base import ProxmoxAction


class NodesNodeFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, node, delete=None, digest=None, enable=None, log_level_in=None, log_level_out=None, log_nf_conntrack=None, ndp=None, nf_conntrack_allow_invalid=None, nf_conntrack_max=None, nf_conntrack_tcp_timeout_established=None, nf_conntrack_tcp_timeout_syn_recv=None, nosmurfs=None, protection_synflood=None, protection_synflood_burst=None, protection_synflood_rate=None, smurf_log_level=None, tcp_flags_log_level=None, tcpflags=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["enable", enable, "boolean"],
            ["log_level_in", log_level_in, "string"],
            ["log_level_out", log_level_out, "string"],
            ["log_nf_conntrack", log_nf_conntrack, "boolean"],
            ["ndp", ndp, "boolean"],
            ["nf_conntrack_allow_invalid", nf_conntrack_allow_invalid, "boolean"],
            ["nf_conntrack_max", nf_conntrack_max, "integer"],
            ["nf_conntrack_tcp_timeout_established", nf_conntrack_tcp_timeout_established, "integer"],
            ["nf_conntrack_tcp_timeout_syn_recv", nf_conntrack_tcp_timeout_syn_recv, "integer"],
            ["node", node, "string"],
            ["nosmurfs", nosmurfs, "boolean"],
            ["protection_synflood", protection_synflood, "boolean"],
            ["protection_synflood_burst", protection_synflood_burst, "integer"],
            ["protection_synflood_rate", protection_synflood_rate, "integer"],
            ["smurf_log_level", smurf_log_level, "string"],
            ["tcp_flags_log_level", tcp_flags_log_level, "string"],
            ["tcpflags", tcpflags, "boolean"],
            
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
            f"nodes/{node}/firewall/options",
            **proxmox_kwargs
        )
        