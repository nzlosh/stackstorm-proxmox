from lib.base import ProxmoxAction


class NodesDisksLvmIndexAction(ProxmoxAction):
    """
    List LVM Volume Groups
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
