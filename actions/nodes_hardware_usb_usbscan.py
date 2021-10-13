from lib.base import ProxmoxAction


class NodesHardwareUsbUsbscanAction(ProxmoxAction):
    """
    List local USB devices.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
