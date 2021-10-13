from lib.base import ProxmoxAction


class NodesStoragePrunebackupsDeleteAction(ProxmoxAction):
    """
    Prune backups. Only those using the standard naming scheme are considered.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
