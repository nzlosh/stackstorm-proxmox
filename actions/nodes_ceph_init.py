from lib.base import ProxmoxAction


class NodesCephInitAction(ProxmoxAction):
    """
    Create initial ceph default configuration and setup symlinks.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
