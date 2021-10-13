from lib.base import ProxmoxAction


class ClusterMetricsServerUpdateAction(ProxmoxAction):
    """
    Update metric server configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
