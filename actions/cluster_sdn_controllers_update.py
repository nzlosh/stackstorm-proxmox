from lib.base import ProxmoxAction


class ClusterSdnControllersUpdateAction(ProxmoxAction):
    """
    Update sdn controller object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
