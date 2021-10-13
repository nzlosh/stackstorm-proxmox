from lib.base import ProxmoxAction


class ClusterSdnVnetsSubnetsUpdateAction(ProxmoxAction):
    """
    Update sdn subnet object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
