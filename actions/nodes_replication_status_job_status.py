from lib.base import ProxmoxAction


class NodesReplicationStatusJobStatusAction(ProxmoxAction):
    """
    Get replication job status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
