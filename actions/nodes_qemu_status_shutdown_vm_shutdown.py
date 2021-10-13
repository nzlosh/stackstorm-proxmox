from lib.base import ProxmoxAction


class NodesQemuStatusShutdownVmShutdownAction(ProxmoxAction):
    """
    Shutdown virtual machine. This is similar to pressing the power button on a physical machine.This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
