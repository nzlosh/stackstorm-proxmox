from lib.base import ProxmoxAction


class NodesTermproxyAction(ProxmoxAction):
    """
    Creates a VNC Shell proxy.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
