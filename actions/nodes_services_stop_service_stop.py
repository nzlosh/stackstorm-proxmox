from lib.base import ProxmoxAction


class NodesServicesStopServiceStopAction(ProxmoxAction):
    """
    Stop service.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
