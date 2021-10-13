from lib.base import ProxmoxAction


class NodesConfigSetOptionsAction(ProxmoxAction):
    """
    Set node configuration options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
