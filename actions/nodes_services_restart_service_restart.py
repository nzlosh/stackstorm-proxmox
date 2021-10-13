from lib.base import ProxmoxAction


class NodesServicesRestartServiceRestartAction(ProxmoxAction):
    """
    Hard restart service. Use reload if you want to reduce interruptions.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
