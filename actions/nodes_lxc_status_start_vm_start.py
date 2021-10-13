from lib.base import ProxmoxAction


class NodesLxcStatusStartVmStartAction(ProxmoxAction):
    """
    Start the container.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
