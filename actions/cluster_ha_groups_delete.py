from lib.base import ProxmoxAction


class ClusterHaGroupsDeleteAction(ProxmoxAction):
    """
    Delete ha group configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
