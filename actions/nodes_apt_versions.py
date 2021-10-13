from lib.base import ProxmoxAction


class NodesAptVersionsAction(ProxmoxAction):
    """
    Get package information for important Proxmox packages.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
