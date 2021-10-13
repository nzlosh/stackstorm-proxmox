from lib.base import ProxmoxAction


class NodesQemuAgentSuspend-ramAction(ProxmoxAction):
    """
    Execute suspend-ram.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
