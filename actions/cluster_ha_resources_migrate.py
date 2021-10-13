from lib.base import ProxmoxAction


class ClusterHaResourcesMigrateAction(ProxmoxAction):
    """
    Request resource migration (online) to another node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
