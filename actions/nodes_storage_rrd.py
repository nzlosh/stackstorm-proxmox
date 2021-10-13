from lib.base import ProxmoxAction


class NodesStorageRrdAction(ProxmoxAction):
    """
    Read storage RRD statistics (returns PNG).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
