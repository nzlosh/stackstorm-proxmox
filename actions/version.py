from lib.base import ProxmoxAction


class VersionAction(ProxmoxAction):
    """
    API version details. The result also includes the global datacenter confguration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
