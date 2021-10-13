from lib.base import ProxmoxAction


class NodesStartallAction(ProxmoxAction):
    """
    Start all VMs and containers located on this node (by default only those with onboot=1).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
