from lib.base import ProxmoxAction


class ClusterHaResourcesRelocateAction(ProxmoxAction):
    """
    Request resource relocatzion to another node. This stops the service on the old node, and restarts it on the target node.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
