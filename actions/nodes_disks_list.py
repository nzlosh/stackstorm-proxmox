from lib.base import ProxmoxAction


class NodesDisksListAction(ProxmoxAction):
    """
    List local disks.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
