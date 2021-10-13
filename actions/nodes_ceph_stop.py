from lib.base import ProxmoxAction


class NodesCephStopAction(ProxmoxAction):
    """
    Stop ceph services.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
