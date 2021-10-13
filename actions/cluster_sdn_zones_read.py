from lib.base import ProxmoxAction


class ClusterSdnZonesReadAction(ProxmoxAction):
    """
    Read sdn zone configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
