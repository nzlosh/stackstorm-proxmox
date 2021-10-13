from lib.base import ProxmoxAction


class NodesAptRepositoriesAddRepositoryAction(ProxmoxAction):
    """
    Add a standard repository to the configuration
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
