from lib.base import ProxmoxAction


class NodesScanNfsNfsscanAction(ProxmoxAction):
    """
    Scan remote NFS server.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
