from lib.base import ProxmoxAction


class NodesConfigGetConfigAction(ProxmoxAction):
    """
    Get node configuration options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
