import json
from packlib.base import ProxmoxAction


class NodesNodeTasksNodeTasksAction(ProxmoxAction):
    """
    Read task list for one node (finished tasks).
    """

    def run(self, node, errors=False, limit=50, since=None, source="archive", start=0, statusfilter=None, typefilter=None, until=None, userfilter=None, vmid=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["errors", errors, "boolean"],
            ["limit", limit, "integer"],
            ["node", node, "string"],
            ["since", since, "integer"],
            ["source", source, "string"],
            ["start", start, "integer"],
            ["statusfilter", statusfilter, "string"],
            ["typefilter", typefilter, "string"],
            ["until", until, "integer"],
            ["userfilter", userfilter, "string"],
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

        return self.proxmox.get(
            f"nodes/{node}/tasks",
            **proxmox_kwargs
        )
        