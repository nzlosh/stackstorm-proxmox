from lib.base import ProxmoxAction


class NodesLxcStatusCurrentVmStatusAction(ProxmoxAction):
    """
    Get virtual machine status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
