from lib.base import ProxmoxAction


class NodesLxcMigrateMigrateVmAction(ProxmoxAction):
    """
    Migrate the container to another node. Creates a new migration task.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
