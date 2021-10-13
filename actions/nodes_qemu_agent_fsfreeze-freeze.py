from lib.base import ProxmoxAction


class NodesQemuAgentFsfreeze-freezeAction(ProxmoxAction):
    """
    Execute fsfreeze-freeze.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
