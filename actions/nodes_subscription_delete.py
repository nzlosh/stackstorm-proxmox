from lib.base import ProxmoxAction


class NodesSubscriptionDeleteAction(ProxmoxAction):
    """
    Delete subscription key of this node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
