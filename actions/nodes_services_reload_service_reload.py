from lib.base import ProxmoxAction


class NodesServicesReloadServiceReloadAction(ProxmoxAction):
    """
    Reload service. Falls back to restart if service cannot be reloaded.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
