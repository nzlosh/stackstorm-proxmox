from lib.base import ProxmoxAction


class ClusterMetricsServerDeleteAction(ProxmoxAction):
    """
    Remove Metric server.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
