from lib.base import ProxmoxAction


class NodesQemuFirewallLogAction(ProxmoxAction):
    """
    Read firewall log
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
