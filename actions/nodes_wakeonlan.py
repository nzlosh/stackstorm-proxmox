from lib.base import ProxmoxAction


class NodesWakeonlanAction(ProxmoxAction):
    """
    Try to wake a node via 'wake on LAN' network packet.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
