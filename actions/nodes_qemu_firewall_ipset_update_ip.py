from lib.base import ProxmoxAction


class NodesQemuFirewallIpsetUpdateIpAction(ProxmoxAction):
    """
    Update IP or Network settings
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
