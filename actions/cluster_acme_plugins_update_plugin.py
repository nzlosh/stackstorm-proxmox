from lib.base import ProxmoxAction


class ClusterAcmePluginsUpdatePluginAction(ProxmoxAction):
    """
    Update ACME plugin configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
