from lib.base import ProxmoxAction


class NodesQemuCloudinitDumpCloudinitGeneratedConfigDumpAction(ProxmoxAction):
    """
    Get automatically generated cloudinit config.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
