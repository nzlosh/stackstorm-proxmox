from lib.base import ProxmoxAction


class NodesCephRulesAction(ProxmoxAction):
    """
    List ceph rules.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
