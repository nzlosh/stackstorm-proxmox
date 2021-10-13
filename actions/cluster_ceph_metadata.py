from lib.base import ProxmoxAction


class ClusterCephMetadataAction(ProxmoxAction):
    """
    Get ceph metadata.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
