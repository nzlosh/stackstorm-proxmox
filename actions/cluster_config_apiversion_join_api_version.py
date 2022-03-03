import json
from packlib.base import ProxmoxAction


class ClusterConfigApiversionJoinApiVersionAction(ProxmoxAction):
    """
    Return the version of the cluster join API available on this node.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/config/apiversion")
