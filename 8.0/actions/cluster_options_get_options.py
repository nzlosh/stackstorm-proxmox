import json
from packlib.base import ProxmoxAction


class ClusterOptionsGetOptionsAction(ProxmoxAction):
    """
    Get datacenter options. Without 'Sys.Audit' on '/' not all options are returned.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"cluster/options")
        