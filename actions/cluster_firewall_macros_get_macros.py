from lib.base import ProxmoxAction


class ClusterFirewallMacrosGetMacrosAction(ProxmoxAction):
    """
    List available macros
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
