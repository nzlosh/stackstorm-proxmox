from lib.base import ProxmoxAction


class ClusterReplicationReadAction(ProxmoxAction):
    """
    Read replication job configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
