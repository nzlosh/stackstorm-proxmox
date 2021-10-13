from lib.base import ProxmoxAction


class NodesReplicationLogReadJobLogAction(ProxmoxAction):
    """
    Read replication job log.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
