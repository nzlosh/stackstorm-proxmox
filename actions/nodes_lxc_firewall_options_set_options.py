from lib.base import ProxmoxAction


class NodesLxcFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
