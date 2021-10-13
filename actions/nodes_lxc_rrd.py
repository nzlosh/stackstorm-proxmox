from lib.base import ProxmoxAction


class NodesLxcRrdAction(ProxmoxAction):
    """
    Read VM RRD statistics (returns PNG)
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
