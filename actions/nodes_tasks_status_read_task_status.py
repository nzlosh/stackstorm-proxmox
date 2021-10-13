from lib.base import ProxmoxAction


class NodesTasksStatusReadTaskStatusAction(ProxmoxAction):
    """
    Read task status.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
