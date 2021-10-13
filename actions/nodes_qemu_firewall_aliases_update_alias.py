from lib.base import ProxmoxAction


class NodesQemuFirewallAliasesUpdateAliasAction(ProxmoxAction):
    """
    Update IP or Network alias.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
