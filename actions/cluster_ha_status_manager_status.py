from lib.base import ProxmoxAction


class ClusterHaStatusManager_statusAction(ProxmoxAction):
    """
    Get full HA manger status, including LRM status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
