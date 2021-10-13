from lib.base import ProxmoxAction


class NodesQemuStatusResumeVmResumeAction(ProxmoxAction):
    """
    Resume virtual machine.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
