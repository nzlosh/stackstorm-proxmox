from lib.base import ProxmoxAction


class NodesSyslogAction(ProxmoxAction):
    """
    Read system log
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
