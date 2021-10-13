from lib.base import ProxmoxAction


class NodesLxcFirewallLogAction(ProxmoxAction):
    """
    Read firewall log
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
