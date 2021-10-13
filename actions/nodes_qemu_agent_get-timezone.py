from lib.base import ProxmoxAction


class NodesQemuAgentGet-timezoneAction(ProxmoxAction):
    """
    Execute get-timezone.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
