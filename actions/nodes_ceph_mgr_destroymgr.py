from lib.base import ProxmoxAction


class NodesCephMgrDestroymgrAction(ProxmoxAction):
    """
    Destroy Ceph Manager.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
