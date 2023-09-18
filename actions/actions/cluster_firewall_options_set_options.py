import json
from packlib.base import ProxmoxAction


class ClusterFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, delete=None, digest=None, ebtables=None, enable=None, log_ratelimit=None, policy_in=None, policy_out=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["ebtables", ebtables, "boolean"],
            ["enable", enable, "integer"],
            ["log_ratelimit", log_ratelimit, "string"],
            ["policy_in", policy_in, "string"],
            ["policy_out", policy_out, "string"],
            
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
            f"cluster/firewall/options",
            **proxmox_kwargs
        )
        