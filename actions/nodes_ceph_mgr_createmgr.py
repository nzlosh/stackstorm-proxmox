from lib.base import ProxmoxAction


class NodesCephMgrCreatemgrAction(ProxmoxAction):
    """
    Create Ceph Manager
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
