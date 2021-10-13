from lib.base import ProxmoxAction


class NodesQemuStatusStartVmStartAction(ProxmoxAction):
    """
    Start virtual machine.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
