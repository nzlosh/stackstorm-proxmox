from lib.base import ProxmoxAction


class NodesQemuStatusStopVmStopAction(ProxmoxAction):
    """
    Stop virtual machine. The qemu process will exit immediately. Thisis akin to pulling the power plug of a running computer and may damage the VM data
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
