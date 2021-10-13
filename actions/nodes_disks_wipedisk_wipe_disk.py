from lib.base import ProxmoxAction


class NodesDisksWipediskWipeDiskAction(ProxmoxAction):
    """
    Wipe a disk or partition.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
