from lib.base import ProxmoxAction


class NodesLxcFirewallIpsetReadIpAction(ProxmoxAction):
    """
    Read IP or Network settings from IPSet.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
