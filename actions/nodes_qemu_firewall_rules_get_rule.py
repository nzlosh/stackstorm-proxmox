from lib.base import ProxmoxAction


class NodesQemuFirewallRulesGetRuleAction(ProxmoxAction):
    """
    Get single rule data.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
