from lib.base import ProxmoxAction


class AccessUsersTokenRemoveTokenAction(ProxmoxAction):
    """
    Remove API token for a specific user.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
