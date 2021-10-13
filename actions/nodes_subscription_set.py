from lib.base import ProxmoxAction


class NodesSubscriptionSetAction(ProxmoxAction):
    """
    Set subscription key.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
