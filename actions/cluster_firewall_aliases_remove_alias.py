from lib.base import ProxmoxAction


class ClusterFirewallAliasesRemoveAliasAction(ProxmoxAction):
    """
    Remove IP or Network alias.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
