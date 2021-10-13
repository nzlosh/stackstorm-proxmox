from lib.base import ProxmoxAction


class NodesFirewallLogAction(ProxmoxAction):
    """
    Read firewall log
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
