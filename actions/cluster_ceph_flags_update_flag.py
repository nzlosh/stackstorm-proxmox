from lib.base import ProxmoxAction


class ClusterCephFlagsUpdateFlagAction(ProxmoxAction):
    """
    Set or clear (unset) a specific ceph flag
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
