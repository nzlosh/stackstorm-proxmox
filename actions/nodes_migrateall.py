from lib.base import ProxmoxAction


class NodesMigrateallAction(ProxmoxAction):
    """
    Migrate all VMs and Containers.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
