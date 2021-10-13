from lib.base import ProxmoxAction


class ClusterHaGroupsUpdateAction(ProxmoxAction):
    """
    Update ha group configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
