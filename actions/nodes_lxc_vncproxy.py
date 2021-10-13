from lib.base import ProxmoxAction


class NodesLxcVncproxyAction(ProxmoxAction):
    """
    Creates a TCP VNC proxy connections.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
