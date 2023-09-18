import json
from packlib.base import ProxmoxAction


class ClusterBackupinfoNot_backed_upGetGuestsNotInBackupAction(ProxmoxAction):
    """
    Shows all guests which are not covered by any backup job.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/backupinfo/not_backed_up")
        