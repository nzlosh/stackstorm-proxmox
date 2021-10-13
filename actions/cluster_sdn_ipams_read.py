from lib.base import ProxmoxAction


class ClusterSdnIpamsReadAction(ProxmoxAction):
    """
    Read sdn ipam configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
