from lib.base import ProxmoxAction


class NodesNetworkUpdateNetworkAction(ProxmoxAction):
    """
    Update network device configuration
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
