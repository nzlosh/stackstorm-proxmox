from lib.base import ProxmoxAction


class NodesQemuVncwebsocketAction(ProxmoxAction):
    """
    Opens a weksocket for VNC traffic.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
