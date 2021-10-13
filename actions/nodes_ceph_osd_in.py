from lib.base import ProxmoxAction


class NodesCephOsdInAction(ProxmoxAction):
    """
    ceph osd in
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
