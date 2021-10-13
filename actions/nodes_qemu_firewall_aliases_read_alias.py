from lib.base import ProxmoxAction


class NodesQemuFirewallAliasesReadAliasAction(ProxmoxAction):
    """
    Read alias.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
