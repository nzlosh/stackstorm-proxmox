from lib.base import ProxmoxAction


class NodesScanZfsZfsscanAction(ProxmoxAction):
    """
    Scan zfs pool list on local node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
