from lib.base import ProxmoxAction


class NodesLxcVncwebsocketAction(ProxmoxAction):
    """
    Opens a weksocket for VNC traffic.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
