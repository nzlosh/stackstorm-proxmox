from lib.base import ProxmoxAction


class NodesQemuMove_diskMoveVmDiskAction(ProxmoxAction):
    """
    Move volume to different storage.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
