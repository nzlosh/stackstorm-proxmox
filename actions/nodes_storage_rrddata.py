from lib.base import ProxmoxAction


class NodesStorageRrddataAction(ProxmoxAction):
    """
    Read storage RRD statistics.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
