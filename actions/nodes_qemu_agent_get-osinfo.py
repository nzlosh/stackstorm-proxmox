from lib.base import ProxmoxAction


class NodesQemuAgentGet-osinfoAction(ProxmoxAction):
    """
    Execute get-osinfo.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
