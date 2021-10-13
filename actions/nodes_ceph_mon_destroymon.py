from lib.base import ProxmoxAction


class NodesCephMonDestroymonAction(ProxmoxAction):
    """
    Destroy Ceph Monitor and Manager.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
