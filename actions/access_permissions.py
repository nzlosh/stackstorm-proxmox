from lib.base import ProxmoxAction


class AccessPermissionsAction(ProxmoxAction):
    """
    Retrieve effective permissions of given user/token.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
