from lib.base import ProxmoxAction


class NodesCephConfigAction(ProxmoxAction):
    """
    Get Ceph configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
