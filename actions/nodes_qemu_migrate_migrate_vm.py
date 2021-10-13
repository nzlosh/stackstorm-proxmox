from lib.base import ProxmoxAction


class NodesQemuMigrateMigrateVmAction(ProxmoxAction):
    """
    Migrate virtual machine. Creates a new migration task.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
