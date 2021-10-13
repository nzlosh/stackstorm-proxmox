from lib.base import ProxmoxAction


class StorageDeleteAction(ProxmoxAction):
    """
    Delete storage configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
