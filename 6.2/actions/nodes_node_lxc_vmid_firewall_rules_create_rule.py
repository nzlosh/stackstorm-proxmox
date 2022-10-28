import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidFirewallRulesCreateRuleAction(ProxmoxAction):
    """
    Create new rule.
    """

    def run(self, action, node, prox_type, vmid, comment=None, dest=None, digest=None, dport=None, enable=None, iface=None, log=None, macro=None, pos=None, proto=None, source=None, sport=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["action", action, "string"],
            ["comment", comment, "string"],
            ["dest", dest, "string"],
            ["digest", digest, "string"],
            ["dport", dport, "string"],
            ["enable", enable, "integer"],
            ["iface", iface, "string"],
            ["log", log, "string"],
            ["macro", macro, "string"],
            ["node", node, "string"],
            ["pos", pos, "integer"],
            ["proto", proto, "string"],
            ["source", source, "string"],
            ["sport", sport, "string"],
            ["type", prox_type, "string"],
            ["vmid", vmid, "integer"],
            
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
            f"nodes/{node}/lxc/{vmid}/firewall/rules",
            **proxmox_kwargs
        )
        