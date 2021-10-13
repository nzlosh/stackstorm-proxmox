from lib.base import ProxmoxAction


class NodesQemuAgentExecAction(ProxmoxAction):
    """
    Executes the given command in the vm via the guest-agent and returns an object with the pid.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
