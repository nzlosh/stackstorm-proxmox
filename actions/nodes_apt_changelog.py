from lib.base import ProxmoxAction


class NodesAptChangelogAction(ProxmoxAction):
    """
    Get package changelogs.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
