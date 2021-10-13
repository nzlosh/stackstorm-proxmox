from lib.base import ProxmoxAction


class NodesDnsAction(ProxmoxAction):
    """
    Read DNS settings.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
