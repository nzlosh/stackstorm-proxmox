from lib.base import ProxmoxAction


class AccessRolesDeleteRoleAction(ProxmoxAction):
    """
    Delete role.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
