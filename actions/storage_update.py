from lib.base import ProxmoxAction


class StorageUpdateAction(ProxmoxAction):
    """
    Update storage configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
