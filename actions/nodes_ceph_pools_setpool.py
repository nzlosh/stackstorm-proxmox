from lib.base import ProxmoxAction


class NodesCephPoolsSetpoolAction(ProxmoxAction):
    """
    Change POOL settings
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
