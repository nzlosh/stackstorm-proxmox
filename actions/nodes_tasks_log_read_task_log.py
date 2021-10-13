from lib.base import ProxmoxAction


class NodesTasksLogReadTaskLogAction(ProxmoxAction):
    """
    Read task log.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
