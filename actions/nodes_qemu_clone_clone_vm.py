from lib.base import ProxmoxAction


class NodesQemuCloneCloneVmAction(ProxmoxAction):
    """
    Create a copy of virtual machine/template.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
