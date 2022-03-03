import json
from packlib.base import ProxmoxAction


class AccessTicketGetTicketAction(ProxmoxAction):
    """
    Dummy. Useful for formatters which want to provide a login page.
    """

    def run(self, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        return self.proxmox.get(f"access/ticket")
