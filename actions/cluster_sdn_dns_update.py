from lib.base import ProxmoxAction


class ClusterSdnDnsUpdateAction(ProxmoxAction):
    """
    Update sdn dns object configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
