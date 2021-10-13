from lib.base import ProxmoxAction


class NodesQemuAgentFile-writeAction(ProxmoxAction):
    """
    Writes the given file via guest agent.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
