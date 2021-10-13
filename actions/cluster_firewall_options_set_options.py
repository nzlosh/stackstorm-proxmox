from lib.base import ProxmoxAction


class ClusterFirewallOptionsSetOptionsAction(ProxmoxAction):
    """
    Set Firewall options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
