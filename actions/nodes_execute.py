from lib.base import ProxmoxAction


class NodesExecuteAction(ProxmoxAction):
    """
    Execute multiple commands in order.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
