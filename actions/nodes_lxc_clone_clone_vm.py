from lib.base import ProxmoxAction


class NodesLxcCloneCloneVmAction(ProxmoxAction):
    """
    Create a container clone/copy
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
