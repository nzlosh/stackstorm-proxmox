from lib.base import ProxmoxAction


class ClusterAcmeAccountDeactivateAccountAction(ProxmoxAction):
    """
    Deactivate existing ACME account at CA.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
