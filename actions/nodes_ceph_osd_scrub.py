from lib.base import ProxmoxAction


class NodesCephOsdScrubAction(ProxmoxAction):
    """
    Instruct the OSD to scrub.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
