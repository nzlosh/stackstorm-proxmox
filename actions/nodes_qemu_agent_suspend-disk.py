from lib.base import ProxmoxAction


class NodesQemuAgentSuspend-diskAction(ProxmoxAction):
    """
    Execute suspend-disk.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
