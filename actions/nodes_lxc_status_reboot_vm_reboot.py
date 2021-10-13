from lib.base import ProxmoxAction


class NodesLxcStatusRebootVmRebootAction(ProxmoxAction):
    """
    Reboot the container by shutting it down, and starting it again. Applies pending changes.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
