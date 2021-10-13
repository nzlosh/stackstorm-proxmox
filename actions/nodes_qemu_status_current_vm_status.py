from lib.base import ProxmoxAction


class NodesQemuStatusCurrentVmStatusAction(ProxmoxAction):
    """
    Get virtual machine status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
