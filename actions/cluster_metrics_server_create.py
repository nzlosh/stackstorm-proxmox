from lib.base import ProxmoxAction


class ClusterMetricsServerCreateAction(ProxmoxAction):
    """
    Create a new external metric server config
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
