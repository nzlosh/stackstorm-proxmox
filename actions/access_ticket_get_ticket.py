from lib.base import ProxmoxAction


class AccessTicketGetTicketAction(ProxmoxAction):
    """
    Dummy. Useful for formatters which want to provide a login page.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
