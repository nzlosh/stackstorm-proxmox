from lib.base import ProxmoxAction


class ClusterStatusGetStatusAction(ProxmoxAction):
    """
    Get cluster status information.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
