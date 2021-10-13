from lib.base import ProxmoxAction


class NodesAplinfoAplDownloadAction(ProxmoxAction):
    """
    Download appliance templates.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
