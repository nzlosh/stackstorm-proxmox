from lib.base import ProxmoxAction


class NodesQemuAgentFile-readAction(ProxmoxAction):
    """
    Reads the given file via guest agent. Is limited to 16777216 bytes.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
