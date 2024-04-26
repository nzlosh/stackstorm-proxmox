import json
from packlib.base import ProxmoxAction


class ClusterNotificationsMatchersCreateMatcherAction(ProxmoxAction):
    """
    Create a new matcher
    """

    def run(
        self,
        name,
        comment=None,
        disable=None,
        invert_match=None,
        match_calendar=None,
        match_field=None,
        match_severity=None,
        mode=None,
        target=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["disable", disable, "boolean"],
            ["invert-match", invert_match, "boolean"],
            ["match-calendar", match_calendar, "array"],
            ["match-field", match_field, "array"],
            ["match-severity", match_severity, "array"],
            ["mode", mode, "string"],
            ["name", name, "string"],
            ["target", target, "array"],
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

        return self.proxmox.post(f"cluster/notifications/matchers", **proxmox_kwargs)
