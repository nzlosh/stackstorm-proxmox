from lib.base import ProxmoxAction


class NodesCephOsdOutAction(ProxmoxAction):
    """
    ceph osd out
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
