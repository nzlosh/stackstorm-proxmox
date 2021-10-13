from lib.base import ProxmoxAction


class NodesAptRepositoriesAction(ProxmoxAction):
    """
    Get APT repository information.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
