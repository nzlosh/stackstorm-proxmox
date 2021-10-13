from lib.base import ProxmoxAction


class NodesLxcFirewallAliasesReadAliasAction(ProxmoxAction):
    """
    Read alias.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
