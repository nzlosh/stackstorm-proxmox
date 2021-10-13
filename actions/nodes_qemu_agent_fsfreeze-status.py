from lib.base import ProxmoxAction


class NodesQemuAgentFsfreeze-statusAction(ProxmoxAction):
    """
    Execute fsfreeze-status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
