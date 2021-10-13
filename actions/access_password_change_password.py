from lib.base import ProxmoxAction


class AccessPasswordChangePasswordAction(ProxmoxAction):
    """
    Change user password.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
