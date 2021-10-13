from lib.base import ProxmoxAction


class NodesQemuAgentFsfreeze-thawAction(ProxmoxAction):
    """
    Execute fsfreeze-thaw.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
