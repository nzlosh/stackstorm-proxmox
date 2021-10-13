from lib.base import ProxmoxAction


class NodesLxcMove_volumeAction(ProxmoxAction):
    """
    Move a rootfs-/mp-volume to a different storage
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
