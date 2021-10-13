from lib.base import ProxmoxAction


class NodesStorageContentDeleteAction(ProxmoxAction):
    """
    Delete volume
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
