from lib.base import ProxmoxAction


class NodesQemuAgentGet-host-nameAction(ProxmoxAction):
    """
    Execute get-host-name.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
