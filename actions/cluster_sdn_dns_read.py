from lib.base import ProxmoxAction


class ClusterSdnDnsReadAction(ProxmoxAction):
    """
    Read sdn dns configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
