from lib.base import ProxmoxAction


class NodesVersionAction(ProxmoxAction):
    """
    API version details
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
