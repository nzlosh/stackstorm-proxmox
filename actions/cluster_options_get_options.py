from lib.base import ProxmoxAction


class ClusterOptionsGetOptionsAction(ProxmoxAction):
    """
    Get datacenter options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
