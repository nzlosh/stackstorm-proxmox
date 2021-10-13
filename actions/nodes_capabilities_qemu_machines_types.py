from lib.base import ProxmoxAction


class NodesCapabilitiesQemuMachinesTypesAction(ProxmoxAction):
    """
    Get available QEMU/KVM machine types.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
