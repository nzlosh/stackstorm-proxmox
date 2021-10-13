from lib.base import ProxmoxAction


class ClusterAcmePluginsGetPluginConfigAction(ProxmoxAction):
    """
    Get ACME plugin configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
