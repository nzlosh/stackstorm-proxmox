from lib.base import ProxmoxAction


class NodesVncwebsocketAction(ProxmoxAction):
    """
    Opens a websocket for VNC traffic.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
