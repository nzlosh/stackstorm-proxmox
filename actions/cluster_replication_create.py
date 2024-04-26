import json
from packlib.base import ProxmoxAction


class ClusterReplicationCreateAction(ProxmoxAction):
    """
    Create a new replication job
    """

    def run(
        self,
        prox_id,
        target,
        prox_type,
        comment=None,
        disable=None,
        rate=None,
        remove_job=None,
        schedule=None,
        source=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["disable", disable, "boolean"],
            ["id", prox_id, "string"],
            ["rate", rate, "number"],
            ["remove_job", remove_job, "string"],
            ["schedule", schedule, "string"],
            ["source", source, "string"],
            ["target", target, "string"],
            ["type", prox_type, "string"],
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

        return self.proxmox.post(f"cluster/replication", **proxmox_kwargs)
