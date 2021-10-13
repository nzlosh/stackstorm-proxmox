from lib.base import ProxmoxAction


class AccessRolesUpdateRoleAction(ProxmoxAction):
    """
    Update an existing role.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
