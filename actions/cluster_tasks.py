from lib.base import ProxmoxAction


class ClusterTasksAction(ProxmoxAction):
    """
    List recent tasks (cluster wide).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
