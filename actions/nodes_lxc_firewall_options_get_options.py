from lib.base import ProxmoxAction


class NodesLxcFirewallOptionsGetOptionsAction(ProxmoxAction):
    """
    Get VM firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
