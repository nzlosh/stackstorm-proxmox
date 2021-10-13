from lib.base import ProxmoxAction


class NodesVzdumpDefaultsAction(ProxmoxAction):
    """
    Get the currently configured vzdump defaults.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
