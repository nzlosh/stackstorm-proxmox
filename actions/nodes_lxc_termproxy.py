from lib.base import ProxmoxAction


class NodesLxcTermproxyAction(ProxmoxAction):
    """
    Creates a TCP proxy connection.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
