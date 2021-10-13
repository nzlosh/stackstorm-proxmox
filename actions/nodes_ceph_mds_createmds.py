from lib.base import ProxmoxAction


class NodesCephMdsCreatemdsAction(ProxmoxAction):
    """
    Create Ceph Metadata Server (MDS)
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
