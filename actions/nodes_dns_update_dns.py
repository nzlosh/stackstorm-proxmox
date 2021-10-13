from lib.base import ProxmoxAction


class NodesDnsUpdateDnsAction(ProxmoxAction):
    """
    Write DNS settings.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
