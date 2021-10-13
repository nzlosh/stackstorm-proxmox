from lib.base import ProxmoxAction


class NodesDisksDirectoryCreateAction(ProxmoxAction):
    """
    Create a Filesystem on an unused disk. Will be mounted under '/mnt/pve/NAME'.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
