from lib.base import ProxmoxAction


class AccessUsersTokenGenerateTokenAction(ProxmoxAction):
    """
    Generate a new API token for a specific user. NOTE: returns API token value, which needs to be stored as it cannot be retrieved afterwards!
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
