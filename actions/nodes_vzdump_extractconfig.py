from lib.base import ProxmoxAction


class NodesVzdumpExtractconfigAction(ProxmoxAction):
    """
    Extract configuration from vzdump backup archive.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
