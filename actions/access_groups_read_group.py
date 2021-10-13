from lib.base import ProxmoxAction


class AccessGroupsReadGroupAction(ProxmoxAction):
    """
    Get group configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
