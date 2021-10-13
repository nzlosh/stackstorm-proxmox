from lib.base import ProxmoxAction


class ClusterNextidAction(ProxmoxAction):
    """
    Get next free VMID. If you pass an VMID it will raise an error if the ID is already used.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
