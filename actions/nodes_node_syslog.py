import json
from packlib.base import ProxmoxAction


class NodesNodeSyslogAction(ProxmoxAction):
    """
    Read system log
    """

    def run(
        self,
        node,
        limit=None,
        service=None,
        since=None,
        start=None,
        until=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["limit", limit, "integer"],
            ["node", node, "string"],
            ["service", service, "string"],
            ["since", since, "string"],
            ["start", start, "integer"],
            ["until", until, "string"],
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

        return self.proxmox.get(f"nodes/{node}/syslog", **proxmox_kwargs)
