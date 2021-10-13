from lib.base import ProxmoxAction


class NodesCertificatesCustomUploadCustomCertAction(ProxmoxAction):
    """
    Upload or update custom certificate chain and key.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
