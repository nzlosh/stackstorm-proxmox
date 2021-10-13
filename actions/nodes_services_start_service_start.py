from lib.base import ProxmoxAction


class NodesServicesStartServiceStartAction(ProxmoxAction):
    """
    Start service.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
