from lib.base import ProxmoxAction


class NodesFirewallRulesGetRuleAction(ProxmoxAction):
    """
    Get single rule data.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
