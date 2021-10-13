from lib.base import ProxmoxAction


class ClusterConfigTotemAction(ProxmoxAction):
    """
    Get corosync totem protocol settings.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
