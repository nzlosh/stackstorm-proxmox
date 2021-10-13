from lib.base import ProxmoxAction


class NodesRrdAction(ProxmoxAction):
    """
    Read node RRD statistics (returns PNG)
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
