from lib.base import ProxmoxAction


class NodesDisksLvmCreateAction(ProxmoxAction):
    """
    Create an LVM Volume Group
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
