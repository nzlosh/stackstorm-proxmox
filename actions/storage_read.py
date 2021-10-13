from lib.base import ProxmoxAction


class StorageReadAction(ProxmoxAction):
    """
    Read storage configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
