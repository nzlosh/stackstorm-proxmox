from lib.base import ProxmoxAction


class NodesLxcStatusStopVmStopAction(ProxmoxAction):
    """
    Stop the container. This will abruptly stop all processes running in the container.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
