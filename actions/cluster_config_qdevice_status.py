from lib.base import ProxmoxAction


class ClusterConfigQdeviceStatusAction(ProxmoxAction):
    """
    Get QDevice status
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
