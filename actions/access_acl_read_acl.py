from lib.base import ProxmoxAction


class AccessAclReadAclAction(ProxmoxAction):
    """
    Get Access Control List (ACLs).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
