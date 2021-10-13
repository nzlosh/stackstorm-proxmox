from lib.base import ProxmoxAction


class NodesLxcConfigUpdateVmAction(ProxmoxAction):
    """
    Set container options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
