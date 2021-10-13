from lib.base import ProxmoxAction


class NodesNetworkNetworkConfigAction(ProxmoxAction):
    """
    Read network device configuration
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
