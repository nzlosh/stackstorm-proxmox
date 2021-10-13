from lib.base import ProxmoxAction


class NodesQemuAgentExec-statusAction(ProxmoxAction):
    """
    Gets the status of the given pid started by the guest-agent
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
