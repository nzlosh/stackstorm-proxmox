from lib.base import ProxmoxAction


class NodesAptRepositoriesChangeRepositoryAction(ProxmoxAction):
    """
    Change the properties of a repository. Currently only allows enabling/disabling.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
