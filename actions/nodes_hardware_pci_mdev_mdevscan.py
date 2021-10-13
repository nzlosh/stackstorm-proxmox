from lib.base import ProxmoxAction


class NodesHardwarePciMdevMdevscanAction(ProxmoxAction):
    """
    List mediated device types for given PCI device.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
