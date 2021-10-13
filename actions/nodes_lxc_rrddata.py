from lib.base import ProxmoxAction


class NodesLxcRrddataAction(ProxmoxAction):
    """
    Read VM RRD statistics
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
