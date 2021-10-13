from lib.base import ProxmoxAction


class NodesQemuStatusRebootVmRebootAction(ProxmoxAction):
    """
    Reboot the VM by shutting it down, and starting it again. Applies pending changes.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
