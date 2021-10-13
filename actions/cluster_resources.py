from lib.base import ProxmoxAction


class ClusterResourcesAction(ProxmoxAction):
    """
    Resources index (cluster wide).
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
