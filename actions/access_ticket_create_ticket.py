from lib.base import ProxmoxAction


class AccessTicketCreateTicketAction(ProxmoxAction):
    """
    Create or verify authentication ticket.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
