from lib.base import ProxmoxAction


class NodesDisksLvmthinIndexAction(ProxmoxAction):
    """
    List LVM thinpools
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
