import json
from packlib.base import ProxmoxAction


class ClusterCephMetadataAction(ProxmoxAction):
    """
    Get ceph metadata.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/ceph/metadata")
        