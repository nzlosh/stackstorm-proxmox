import json
from packlib.base import ProxmoxAction


class VersionAction(ProxmoxAction):
    """
    API version details, including some parts of the global datacenter config.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"version")
        