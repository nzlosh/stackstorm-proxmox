from lib.base import ProxmoxAction


class NodesCephMonCreatemonAction(ProxmoxAction):
    """
    Create Ceph Monitor and Manager
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
