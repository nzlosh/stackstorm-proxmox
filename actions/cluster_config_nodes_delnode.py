from lib.base import ProxmoxAction


class ClusterConfigNodesDelnodeAction(ProxmoxAction):
    """
    Removes a node from the cluster configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
