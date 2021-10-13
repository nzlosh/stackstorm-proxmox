from lib.base import ProxmoxAction


class ClusterConfigJoinJoinInfoAction(ProxmoxAction):
    """
    Get information needed to join this cluster over the connected node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
