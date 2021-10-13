from lib.base import ProxmoxAction


class NodesAplinfoAction(ProxmoxAction):
    """
    Get list of appliances.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
