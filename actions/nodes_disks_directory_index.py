from lib.base import ProxmoxAction


class NodesDisksDirectoryIndexAction(ProxmoxAction):
    """
    PVE Managed Directory storages.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
