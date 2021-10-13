from lib.base import ProxmoxAction


class NodesAptUpdateUpdateDatabaseAction(ProxmoxAction):
    """
    This is used to resynchronize the package index files from their sources (apt-get update).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
