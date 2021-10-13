from lib.base import ProxmoxAction


class NodesCephPoolsGetpoolAction(ProxmoxAction):
    """
    List pool settings.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
