from lib.base import ProxmoxAction


class NodesQemuAgentGet-usersAction(ProxmoxAction):
    """
    Execute get-users.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
