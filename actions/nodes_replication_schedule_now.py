from lib.base import ProxmoxAction


class NodesReplicationSchedule_nowAction(ProxmoxAction):
    """
    Schedule replication job to start as soon as possible.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
