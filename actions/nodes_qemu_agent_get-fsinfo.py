from lib.base import ProxmoxAction


class NodesQemuAgentGet-fsinfoAction(ProxmoxAction):
    """
    Execute get-fsinfo.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
