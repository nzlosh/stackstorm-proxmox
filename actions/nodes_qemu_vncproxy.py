from lib.base import ProxmoxAction


class NodesQemuVncproxyAction(ProxmoxAction):
    """
    Creates a TCP VNC proxy connections.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
