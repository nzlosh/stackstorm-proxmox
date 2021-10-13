from lib.base import ProxmoxAction


class NodesStatusNodeCmdAction(ProxmoxAction):
    """
    Reboot or shutdown a node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
