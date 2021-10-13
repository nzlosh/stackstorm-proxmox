from lib.base import ProxmoxAction


class ClusterFirewallRefsAction(ProxmoxAction):
    """
    Lists possible IPSet/Alias reference which are allowed in source/dest properties.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
