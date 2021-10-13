from lib.base import ProxmoxAction


class NodesCephFsCreatefsAction(ProxmoxAction):
    """
    Create a Ceph filesystem
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
