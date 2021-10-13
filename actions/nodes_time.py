from lib.base import ProxmoxAction


class NodesTimeAction(ProxmoxAction):
    """
    Read server time and time zone settings.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
