from lib.base import ProxmoxAction


class ClusterReplicationDeleteAction(ProxmoxAction):
    """
    Mark replication job for removal.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
