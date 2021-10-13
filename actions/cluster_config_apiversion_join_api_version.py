from lib.base import ProxmoxAction


class ClusterConfigApiversionJoinApiVersionAction(ProxmoxAction):
    """
    Return the version of the cluster join API available on this node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
