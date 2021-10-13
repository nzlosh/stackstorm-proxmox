from lib.base import ProxmoxAction


class ClusterConfigJoinAction(ProxmoxAction):
    """
    Joins this node into an existing cluster. If no links are given, default to IP resolved by node's hostname on single link (fallback fails for clusters with multiple links).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
