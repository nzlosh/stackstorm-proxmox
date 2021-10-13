from lib.base import ProxmoxAction


class NodesQemuSnapshotConfigGetSnapshotConfigAction(ProxmoxAction):
    """
    Get snapshot configuration
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
