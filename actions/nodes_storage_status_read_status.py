from lib.base import ProxmoxAction


class NodesStorageStatusReadStatusAction(ProxmoxAction):
    """
    Read storage status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
