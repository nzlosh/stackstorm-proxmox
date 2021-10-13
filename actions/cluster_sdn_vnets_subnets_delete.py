from lib.base import ProxmoxAction


class ClusterSdnVnetsSubnetsDeleteAction(ProxmoxAction):
    """
    Delete sdn subnet object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
