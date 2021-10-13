from lib.base import ProxmoxAction


class NodesCapabilitiesQemuCpuIndexAction(ProxmoxAction):
    """
    List all custom and default CPU models.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
