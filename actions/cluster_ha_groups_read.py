from lib.base import ProxmoxAction


class ClusterHaGroupsReadAction(ProxmoxAction):
    """
    Read ha group configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
