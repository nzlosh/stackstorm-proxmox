from lib.base import ProxmoxAction


class NodesScanGlusterfsGlusterfsscanAction(ProxmoxAction):
    """
    Scan remote GlusterFS server.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
