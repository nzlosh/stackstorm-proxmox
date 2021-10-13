from lib.base import ProxmoxAction


class NodesLxcSnapshotConfigUpdateSnapshotConfigAction(ProxmoxAction):
    """
    Update snapshot metadata.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
