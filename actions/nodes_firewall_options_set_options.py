from lib.base import ProxmoxAction


class NodesFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
