from lib.base import ProxmoxAction


class NodesQemuAgentSuspend-hybridAction(ProxmoxAction):
    """
    Execute suspend-hybrid.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
