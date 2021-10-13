from lib.base import ProxmoxAction


class AccessRolesReadRoleAction(ProxmoxAction):
    """
    Get role configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
