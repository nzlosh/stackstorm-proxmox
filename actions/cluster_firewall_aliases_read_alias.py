from lib.base import ProxmoxAction


class ClusterFirewallAliasesReadAliasAction(ProxmoxAction):
    """
    Read alias.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
