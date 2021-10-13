from lib.base import ProxmoxAction


class NodesQemuStatusResetVmResetAction(ProxmoxAction):
    """
    Reset virtual machine.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
