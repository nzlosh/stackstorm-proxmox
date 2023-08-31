import json
from packlib.base import ProxmoxAction


class ClusterJobsRealmSyncIdCreateJobAction(ProxmoxAction):
    """
    Create new realm-sync job.
    """

    def run(self, prox_id, schedule, comment=None, enable_new=None, enabled=None, realm=None, remove_vanished=None, scope=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["comment", comment, "string"],
            ["enable-new", enable_new, "boolean"],
            ["enabled", enabled, "boolean"],
            ["id", prox_id, "string"],
            ["realm", realm, "string"],
            ["remove-vanished", remove_vanished, "string"],
            ["schedule", schedule, "string"],
            ["scope", scope, "string"],
            
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
            f"cluster/jobs/realm-sync/{id}",
            **proxmox_kwargs
        )
        