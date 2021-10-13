from lib.base import ProxmoxAction


class ClusterFirewallIpsetRemoveIpAction(ProxmoxAction):
    """
    Remove IP or Network from IPSet.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
