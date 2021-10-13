from lib.base import ProxmoxAction


class NodesLxcSnapshotConfigGetSnapshotConfigAction(ProxmoxAction):
    """
    Get snapshot configuration
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
