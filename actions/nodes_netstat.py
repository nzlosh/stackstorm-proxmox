from lib.base import ProxmoxAction


class NodesNetstatAction(ProxmoxAction):
    """
    Read tap/vm network device interface counters
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
