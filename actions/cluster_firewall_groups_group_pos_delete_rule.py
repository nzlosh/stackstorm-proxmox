import json
from packlib.base import ProxmoxAction


class ClusterFirewallGroupsGroupPosDeleteRuleAction(ProxmoxAction):
    """
    Delete rule.
    """

    def run(self, group, digest=None, pos=None, profile_name=None, api_timeout=5):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["digest", digest, "string"],
            ["group", group, "string"],
            ["pos", pos, "integer"],
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

        return self.proxmox.delete(f"cluster/firewall/groups/{group}/{pos}", **proxmox_kwargs)
