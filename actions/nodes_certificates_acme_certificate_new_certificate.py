from lib.base import ProxmoxAction


class NodesCertificatesAcmeCertificateNewCertificateAction(ProxmoxAction):
    """
    Order a new certificate from ACME-compatible CA.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
