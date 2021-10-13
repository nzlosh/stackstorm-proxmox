from lib.base import ProxmoxAction


class NodesDisksZfsDetailAction(ProxmoxAction):
    """
    Get details about a zpool.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
