import json
from packlib.base import ProxmoxAction


class ClusterFirewallRulesPosGetRuleAction(ProxmoxAction):
    """
    Get single rule data.
    """

    def run(self, pos=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["pos", pos, "integer"],
            
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

        return self.proxmox.get(
            f"cluster/firewall/rules/{pos}",
            **proxmox_kwargs
        )
        