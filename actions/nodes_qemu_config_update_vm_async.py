from lib.base import ProxmoxAction


class NodesQemuConfigUpdateVmAsyncAction(ProxmoxAction):
    """
    Set virtual machine options (asynchrounous API).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
