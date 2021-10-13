from lib.base import ProxmoxAction


class NodesSubscriptionUpdateAction(ProxmoxAction):
    """
    Update subscription info.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
