from lib.base import ProxmoxAction


class NodesQemuAgentPingAction(ProxmoxAction):
    """
    Execute ping.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
