from lib.base import ProxmoxAction


class ClusterAcmePluginsDeletePluginAction(ProxmoxAction):
    """
    Delete ACME plugin configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
