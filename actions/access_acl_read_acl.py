import json
from packlib.base import ProxmoxAction


class AccessAclReadAclAction(ProxmoxAction):
    """
    Get Access Control List (ACLs).
    """

    def run(self, profile_name=None, api_timeout=5):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"access/acl")
