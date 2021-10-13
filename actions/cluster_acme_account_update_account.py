from lib.base import ProxmoxAction


class ClusterAcmeAccountUpdateAccountAction(ProxmoxAction):
    """
    Update existing ACME account information with CA. Note: not specifying any new account information triggers a refresh.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
