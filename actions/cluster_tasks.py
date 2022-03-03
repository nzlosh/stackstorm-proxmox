import json
from packlib.base import ProxmoxAction


class ClusterTasksAction(ProxmoxAction):
    """
    List recent tasks (cluster wide).
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/tasks")
