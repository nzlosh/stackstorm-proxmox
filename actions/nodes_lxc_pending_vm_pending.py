from lib.base import ProxmoxAction


class NodesLxcPendingVmPendingAction(ProxmoxAction):
    """
    Get container configuration, including pending changes.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
