from lib.base import ProxmoxAction


class NodesCertificatesAcmeCertificateRevokeCertificateAction(ProxmoxAction):
    """
    Revoke existing certificate from CA.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
