from lib.base import ProxmoxAction


class NodesQemuAgentInfoAction(ProxmoxAction):
    """
    Execute info.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
