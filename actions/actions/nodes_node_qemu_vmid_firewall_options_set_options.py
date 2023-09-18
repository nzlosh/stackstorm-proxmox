import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, node, vmid, delete=None, dhcp=False, digest=None, enable=False, ipfilter=None, log_level_in=None, log_level_out=None, macfilter=False, ndp=False, policy_in=None, policy_out=None, radv=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["delete", delete, "string"],
            ["dhcp", dhcp, "boolean"],
            ["digest", digest, "string"],
            ["enable", enable, "boolean"],
            ["ipfilter", ipfilter, "boolean"],
            ["log_level_in", log_level_in, "string"],
            ["log_level_out", log_level_out, "string"],
            ["macfilter", macfilter, "boolean"],
            ["ndp", ndp, "boolean"],
            ["node", node, "string"],
            ["policy_in", policy_in, "string"],
            ["policy_out", policy_out, "string"],
            ["radv", radv, "boolean"],
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

        return self.proxmox.put(
            f"nodes/{node}/qemu/{vmid}/firewall/options",
            **proxmox_kwargs
        )
        