from lib.base import ProxmoxAction


class NodesScanIscsiIscsiscanAction(ProxmoxAction):
    """
    Scan remote iSCSI server.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
