from lib.base import ProxmoxAction


class NodesCephConfigdbAction(ProxmoxAction):
    """
    Get Ceph configuration database.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
