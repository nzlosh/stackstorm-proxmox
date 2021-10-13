from lib.base import ProxmoxAction


class NodesSubscriptionGetAction(ProxmoxAction):
    """
    Read subscription info.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
