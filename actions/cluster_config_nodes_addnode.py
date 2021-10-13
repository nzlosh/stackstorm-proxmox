from lib.base import ProxmoxAction


class ClusterConfigNodesAddnodeAction(ProxmoxAction):
    """
    Adds a node to the cluster configuration. This call is for internal use.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
