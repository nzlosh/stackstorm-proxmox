from lib.base import ProxmoxAction


class NodesQemuAgentGet-vcpusAction(ProxmoxAction):
    """
    Execute get-vcpus.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
