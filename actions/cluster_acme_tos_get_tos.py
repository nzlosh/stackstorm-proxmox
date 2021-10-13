from lib.base import ProxmoxAction


class ClusterAcmeTosGetTosAction(ProxmoxAction):
    """
    Retrieve ACME TermsOfService URL from CA.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
