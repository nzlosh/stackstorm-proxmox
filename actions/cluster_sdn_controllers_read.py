from lib.base import ProxmoxAction


class ClusterSdnControllersReadAction(ProxmoxAction):
    """
    Read sdn controller configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
