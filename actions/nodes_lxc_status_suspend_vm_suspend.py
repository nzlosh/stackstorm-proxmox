from lib.base import ProxmoxAction


class NodesLxcStatusSuspendVmSuspendAction(ProxmoxAction):
    """
    Suspend the container.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
