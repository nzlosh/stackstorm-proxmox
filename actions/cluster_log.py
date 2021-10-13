from lib.base import ProxmoxAction


class ClusterLogAction(ProxmoxAction):
    """
    Read cluster log
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
