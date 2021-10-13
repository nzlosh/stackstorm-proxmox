from lib.base import ProxmoxAction


class AccessTfaChangeTfaAction(ProxmoxAction):
    """
    Change user u2f authentication.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
