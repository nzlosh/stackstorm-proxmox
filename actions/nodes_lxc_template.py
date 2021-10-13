from lib.base import ProxmoxAction


class NodesLxcTemplateAction(ProxmoxAction):
    """
    Create a Template.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
