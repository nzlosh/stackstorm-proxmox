from lib.base import ProxmoxAction


class NodesCephRestartAction(ProxmoxAction):
    """
    Restart ceph services.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
