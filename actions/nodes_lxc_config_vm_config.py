from lib.base import ProxmoxAction


class NodesLxcConfigVmConfigAction(ProxmoxAction):
    """
    Get container configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
