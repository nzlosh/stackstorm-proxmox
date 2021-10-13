from lib.base import ProxmoxAction


class NodesDisksSmartAction(ProxmoxAction):
    """
    Get SMART Health of a disk.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
