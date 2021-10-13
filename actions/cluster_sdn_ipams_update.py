from lib.base import ProxmoxAction


class ClusterSdnIpamsUpdateAction(ProxmoxAction):
    """
    Update sdn ipam object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
