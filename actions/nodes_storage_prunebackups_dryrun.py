from lib.base import ProxmoxAction


class NodesStoragePrunebackupsDryrunAction(ProxmoxAction):
    """
    Get prune information for backups. NOTE: this is only a preview and might not be what a subsequent prune call does if backups are removed/added in the meantime.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
