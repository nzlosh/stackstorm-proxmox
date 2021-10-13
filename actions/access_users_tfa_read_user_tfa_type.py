from lib.base import ProxmoxAction


class AccessUsersTfaReadUserTfaTypeAction(ProxmoxAction):
    """
    Get user TFA types (Personal and Realm).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
