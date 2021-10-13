from lib.base import ProxmoxAction


class NodesLxcFirewallRulesDeleteRuleAction(ProxmoxAction):
    """
    Delete rule.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
