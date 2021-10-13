from lib.base import ProxmoxAction


class ClusterCephFlagsGetFlagAction(ProxmoxAction):
    """
    Get the status of a specific ceph flag.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
