from lib.base import ProxmoxAction


class NodesQemuPendingVmPendingAction(ProxmoxAction):
    """
    Get the virtual machine configuration with both current and pending values.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
