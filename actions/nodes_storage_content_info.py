from lib.base import ProxmoxAction


class NodesStorageContentInfoAction(ProxmoxAction):
    """
    Get volume attributes
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
