from lib.base import ProxmoxAction


class NodesNetworkDeleteNetworkAction(ProxmoxAction):
    """
    Delete network device configuration
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
