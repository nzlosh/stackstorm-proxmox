from lib.base import ProxmoxAction


class NodesStopallAction(ProxmoxAction):
    """
    Stop all VMs and Containers.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
