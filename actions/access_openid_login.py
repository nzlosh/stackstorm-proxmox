from lib.base import ProxmoxAction


class AccessOpenidLoginAction(ProxmoxAction):
    """
     Verify OpenID authorization code and create a ticket.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
