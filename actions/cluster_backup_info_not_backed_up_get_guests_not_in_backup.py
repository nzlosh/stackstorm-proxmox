import json
from packlib.base import ProxmoxAction


class ClusterBackupInfoNotBackedUpGetGuestsNotInBackupAction(ProxmoxAction):
    """
    Shows all guests which are not covered by any backup job.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/backup-info/not-backed-up")
