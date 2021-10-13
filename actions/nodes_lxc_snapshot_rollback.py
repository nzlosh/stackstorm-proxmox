from lib.base import ProxmoxAction


class NodesLxcSnapshotRollbackAction(ProxmoxAction):
    """
    Rollback LXC state to specified snapshot.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
