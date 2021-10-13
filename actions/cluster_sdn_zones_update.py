from lib.base import ProxmoxAction


class ClusterSdnZonesUpdateAction(ProxmoxAction):
    """
    Update sdn zone object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
