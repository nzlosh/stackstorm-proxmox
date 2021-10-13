from lib.base import ProxmoxAction


class NodesFirewallRulesUpdateRuleAction(ProxmoxAction):
    """
    Modify rule data.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
