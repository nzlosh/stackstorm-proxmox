from lib.base import ProxmoxAction


class NodesScanPbsPbsscanAction(ProxmoxAction):
    """
    Scan remote Proxmox Backup Server.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
