from lib.base import ProxmoxAction


class NodesScanLvmLvmscanAction(ProxmoxAction):
    """
    List local LVM volume groups.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
