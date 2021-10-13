from lib.base import ProxmoxAction


class NodesLxcFirewallAliasesRemoveAliasAction(ProxmoxAction):
    """
    Remove IP or Network alias.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
