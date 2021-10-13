from lib.base import ProxmoxAction


class NodesDisksLvmthinCreateAction(ProxmoxAction):
    """
    Create an LVM thinpool
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
