from lib.base import ProxmoxAction


class ClusterAcmeDirectoriesGetDirectoriesAction(ProxmoxAction):
    """
    Get named known ACME directory endpoints.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
