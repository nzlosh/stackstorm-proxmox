from lib.base import ProxmoxAction


class NodesQemuSendkeyVmSendkeyAction(ProxmoxAction):
    """
    Send key event to virtual machine.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
