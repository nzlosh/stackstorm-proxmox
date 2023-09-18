import json
from packlib.base import ProxmoxAction


class ClusterReplicationIdUpdateAction(ProxmoxAction):
    """
    Update replication job configuration.
    """

    def run(self, prox_id, comment=None, delete=None, digest=None, disable=None, rate=None, remove_job=None, schedule="*/15", source=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["disable", disable, "boolean"],
            ["id", prox_id, "string"],
            ["rate", rate, "number"],
            ["remove_job", remove_job, "string"],
            ["schedule", schedule, "string"],
            ["source", source, "string"],
            
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
            f"cluster/replication/{id}",
            **proxmox_kwargs
        )
        