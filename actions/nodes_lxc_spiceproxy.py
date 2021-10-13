from lib.base import ProxmoxAction


class NodesLxcSpiceproxyAction(ProxmoxAction):
    """
    Returns a SPICE configuration to connect to the CT.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
