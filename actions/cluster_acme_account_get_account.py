from lib.base import ProxmoxAction


class ClusterAcmeAccountGetAccountAction(ProxmoxAction):
    """
    Return existing ACME account information.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
