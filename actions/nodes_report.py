from lib.base import ProxmoxAction


class NodesReportAction(ProxmoxAction):
    """
    Gather various systems information about a node
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
