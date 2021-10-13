from lib.base import ProxmoxAction


class NodesJournalAction(ProxmoxAction):
    """
    Read Journal
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
