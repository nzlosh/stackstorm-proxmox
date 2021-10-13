from lib.base import ProxmoxAction


class NodesRrddataAction(ProxmoxAction):
    """
    Read node RRD statistics
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
