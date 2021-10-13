from lib.base import ProxmoxAction


class NodesQemuAgentFstrimAction(ProxmoxAction):
    """
    Execute fstrim.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
