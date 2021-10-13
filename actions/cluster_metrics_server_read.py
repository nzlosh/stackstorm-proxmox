from lib.base import ProxmoxAction


class ClusterMetricsServerReadAction(ProxmoxAction):
    """
    Read metric server configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
