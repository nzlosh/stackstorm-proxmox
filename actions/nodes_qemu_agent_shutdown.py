from lib.base import ProxmoxAction


class NodesQemuAgentShutdownAction(ProxmoxAction):
    """
    Execute shutdown.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
