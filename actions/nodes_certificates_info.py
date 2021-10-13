from lib.base import ProxmoxAction


class NodesCertificatesInfoAction(ProxmoxAction):
    """
    Get information about node's certificates.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
