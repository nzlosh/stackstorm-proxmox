from lib.base import ProxmoxAction


class AccessAclUpdateAclAction(ProxmoxAction):
    """
    Update Access Control List (add or remove permissions).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
