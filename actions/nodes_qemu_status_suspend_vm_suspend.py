from lib.base import ProxmoxAction


class NodesQemuStatusSuspendVmSuspendAction(ProxmoxAction):
    """
    Suspend virtual machine.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
