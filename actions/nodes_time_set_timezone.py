from lib.base import ProxmoxAction


class NodesTimeSetTimezoneAction(ProxmoxAction):
    """
    Set time zone.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
