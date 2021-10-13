from lib.base import ProxmoxAction


class NodesScanCifsCifsscanAction(ProxmoxAction):
    """
    Scan remote CIFS server.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
