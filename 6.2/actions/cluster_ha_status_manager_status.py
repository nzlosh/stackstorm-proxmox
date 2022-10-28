import json
from packlib.base import ProxmoxAction


class ClusterHaStatusManager_statusAction(ProxmoxAction):
    """
    Get full HA manger status, including LRM status.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/ha/status/manager_status")
        