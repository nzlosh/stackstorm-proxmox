from lib.base import ProxmoxAction


class ClusterFirewallOptionsGetOptionsAction(ProxmoxAction):
    """
    Get Firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
