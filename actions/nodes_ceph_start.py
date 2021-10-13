from lib.base import ProxmoxAction


class NodesCephStartAction(ProxmoxAction):
    """
    Start ceph services.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
