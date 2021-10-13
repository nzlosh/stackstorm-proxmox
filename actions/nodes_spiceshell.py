from lib.base import ProxmoxAction


class NodesSpiceshellAction(ProxmoxAction):
    """
    Creates a SPICE shell.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
