from lib.base import ProxmoxAction


class ClusterOptionsSetOptionsAction(ProxmoxAction):
    """
    Set datacenter options.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
