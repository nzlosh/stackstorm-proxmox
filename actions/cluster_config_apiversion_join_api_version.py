import json
from packlib.base import ProxmoxAction


class ClusterConfigApiversionJoinApiVersionAction(ProxmoxAction):
    """
    Return the version of the cluster join API available on this node.
    """

    def run(self, profile_name=None, api_timeout=5):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/config/apiversion")
