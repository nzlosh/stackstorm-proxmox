from lib.base import ProxmoxAction


class NodesQemuFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
