from lib.base import ProxmoxAction


class NodesCephMdsDestroymdsAction(ProxmoxAction):
    """
    Destroy Ceph Metadata Server
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
