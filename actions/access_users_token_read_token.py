from lib.base import ProxmoxAction


class AccessUsersTokenReadTokenAction(ProxmoxAction):
    """
    Get specific API token information.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
