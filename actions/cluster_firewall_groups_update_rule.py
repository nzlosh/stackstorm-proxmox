from lib.base import ProxmoxAction


class ClusterFirewallGroupsUpdateRuleAction(ProxmoxAction):
    """
    Modify rule data.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
