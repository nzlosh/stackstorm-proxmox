from lib.base import ProxmoxAction


class NodesCertificatesCustomRemoveCustomCertAction(ProxmoxAction):
    """
    DELETE custom certificate chain and key.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
