from lib.base import ProxmoxAction


class NodesLxcStatusShutdownVmShutdownAction(ProxmoxAction):
    """
    Shutdown the container. This will trigger a clean shutdown of the container, see lxc-stop(1) for details.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
