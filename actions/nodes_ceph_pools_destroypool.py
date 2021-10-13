from lib.base import ProxmoxAction


class NodesCephPoolsDestroypoolAction(ProxmoxAction):
    """
    Destroy pool
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
