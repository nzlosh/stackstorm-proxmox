from lib.base import ProxmoxAction


class NodesQemuMigrateMigrateVmPreconditionAction(ProxmoxAction):
    """
    Get preconditions for migration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
