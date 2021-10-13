from lib.base import ProxmoxAction


class NodesQemuAgentGet-timeAction(ProxmoxAction):
    """
    Execute get-time.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
