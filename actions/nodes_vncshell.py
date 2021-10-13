from lib.base import ProxmoxAction


class NodesVncshellAction(ProxmoxAction):
    """
    Creates a VNC Shell proxy.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
