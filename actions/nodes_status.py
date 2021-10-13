from lib.base import ProxmoxAction


class NodesStatusAction(ProxmoxAction):
    """
    Read node status
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
