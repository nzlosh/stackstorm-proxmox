from lib.base import ProxmoxAction


class ClusterCephStatusAction(ProxmoxAction):
    """
    Get ceph status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
