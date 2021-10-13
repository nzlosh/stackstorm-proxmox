from lib.base import ProxmoxAction


class ClusterHaStatusCurrentStatusAction(ProxmoxAction):
    """
    Get HA manger status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
