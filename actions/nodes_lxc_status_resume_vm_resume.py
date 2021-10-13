from lib.base import ProxmoxAction


class NodesLxcStatusResumeVmResumeAction(ProxmoxAction):
    """
    Resume the container.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
