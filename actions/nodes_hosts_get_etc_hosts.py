from lib.base import ProxmoxAction


class NodesHostsGetEtcHostsAction(ProxmoxAction):
    """
    Get the content of /etc/hosts.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
