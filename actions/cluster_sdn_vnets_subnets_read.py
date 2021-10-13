from lib.base import ProxmoxAction


class ClusterSdnVnetsSubnetsReadAction(ProxmoxAction):
    """
    Read sdn subnet configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
