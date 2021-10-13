from lib.base import ProxmoxAction


class NodesQemuSpiceproxyAction(ProxmoxAction):
    """
    Returns a SPICE configuration to connect to the VM.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
