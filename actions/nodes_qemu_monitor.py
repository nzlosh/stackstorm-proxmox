from lib.base import ProxmoxAction


class NodesQemuMonitorAction(ProxmoxAction):
    """
    Execute Qemu monitor commands.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
