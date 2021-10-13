from lib.base import ProxmoxAction


class NodesStorageContentCopyAction(ProxmoxAction):
    """
    Copy a volume. This is experimental code - do not use.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
