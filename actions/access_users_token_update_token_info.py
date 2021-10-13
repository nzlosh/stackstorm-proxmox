from lib.base import ProxmoxAction


class AccessUsersTokenUpdateTokenInfoAction(ProxmoxAction):
    """
    Update API token for a specific user.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
