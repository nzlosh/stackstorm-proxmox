from lib.base import ProxmoxAction


class NodesQemuRrddataAction(ProxmoxAction):
    """
    Read VM RRD statistics
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
