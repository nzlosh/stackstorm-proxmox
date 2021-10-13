from lib.base import ProxmoxAction


class NodesQemuResizeResizeVmAction(ProxmoxAction):
    """
    Extend volume size.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
