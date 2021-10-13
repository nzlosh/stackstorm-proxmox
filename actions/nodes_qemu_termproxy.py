from lib.base import ProxmoxAction


class NodesQemuTermproxyAction(ProxmoxAction):
    """
    Creates a TCP proxy connections.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
