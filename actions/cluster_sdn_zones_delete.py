from lib.base import ProxmoxAction


class ClusterSdnZonesDeleteAction(ProxmoxAction):
    """
    Delete sdn zone object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
