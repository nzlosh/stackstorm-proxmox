from lib.base import ProxmoxAction


class NodesQemuAgentNetwork-get-interfacesAction(ProxmoxAction):
    """
    Execute network-get-interfaces.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
