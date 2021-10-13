from lib.base import ProxmoxAction


class ClusterSdnControllersDeleteAction(ProxmoxAction):
    """
    Delete sdn controller object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
