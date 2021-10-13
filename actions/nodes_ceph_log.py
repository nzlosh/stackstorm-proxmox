from lib.base import ProxmoxAction


class NodesCephLogAction(ProxmoxAction):
    """
    Read ceph log
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
