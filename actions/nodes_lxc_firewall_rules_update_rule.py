from lib.base import ProxmoxAction


class NodesLxcFirewallRulesUpdateRuleAction(ProxmoxAction):
    """
    Modify rule data.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
