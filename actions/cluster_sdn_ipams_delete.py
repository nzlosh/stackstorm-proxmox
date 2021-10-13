from lib.base import ProxmoxAction


class ClusterSdnIpamsDeleteAction(ProxmoxAction):
    """
    Delete sdn ipam object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
