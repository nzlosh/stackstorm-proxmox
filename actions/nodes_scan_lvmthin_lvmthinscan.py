from lib.base import ProxmoxAction


class NodesScanLvmthinLvmthinscanAction(ProxmoxAction):
    """
    List local LVM Thin Pools.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
