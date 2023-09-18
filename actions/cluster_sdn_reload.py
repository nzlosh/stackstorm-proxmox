import json
from packlib.base import ProxmoxAction


class ClusterSdnReloadAction(ProxmoxAction):
    """
    Apply sdn controller changes && reload.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.put(f"cluster/sdn")
        