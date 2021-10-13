from lib.base import ProxmoxAction


class NodesHostsWriteEtcHostsAction(ProxmoxAction):
    """
    Write /etc/hosts.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
