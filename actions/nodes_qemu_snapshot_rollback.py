from lib.base import ProxmoxAction


class NodesQemuSnapshotRollbackAction(ProxmoxAction):
    """
    Rollback VM state to specified snapshot.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
