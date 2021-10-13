from lib.base import ProxmoxAction


class NodesStorageUploadAction(ProxmoxAction):
    """
    Upload templates and ISO images.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
