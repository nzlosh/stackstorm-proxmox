from lib.base import ProxmoxAction


class NodesQemuConfigUpdateVmAction(ProxmoxAction):
    """
    Set virtual machine options (synchrounous API) - You should consider using the POST method instead for any actions involving hotplug or storage allocation.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
