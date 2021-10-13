from lib.base import ProxmoxAction


class AccessGroupsDeleteGroupAction(ProxmoxAction):
    """
    Delete group.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
