from lib.base import ProxmoxAction


class NodesCephCrushAction(ProxmoxAction):
    """
    Get OSD crush map
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
