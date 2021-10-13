from lib.base import ProxmoxAction


class NodesQemuFirewallOptionsGetOptionsAction(ProxmoxAction):
    """
    Get VM firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
