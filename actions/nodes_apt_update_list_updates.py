from lib.base import ProxmoxAction


class NodesAptUpdateListUpdatesAction(ProxmoxAction):
    """
    List available updates.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
