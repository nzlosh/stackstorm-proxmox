from lib.base import ProxmoxAction


class ClusterSdnDnsDeleteAction(ProxmoxAction):
    """
    Delete sdn dns object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
