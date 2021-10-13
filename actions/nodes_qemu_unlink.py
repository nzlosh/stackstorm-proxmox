from lib.base import ProxmoxAction


class NodesQemuUnlinkAction(ProxmoxAction):
    """
    Unlink/delete disk images.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
