from lib.base import ProxmoxAction


class ClusterReplicationUpdateAction(ProxmoxAction):
    """
    Update replication job configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
