from lib.base import ProxmoxAction


class AccessTfaVerifyTfaAction(ProxmoxAction):
    """
    Finish a u2f challenge.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
