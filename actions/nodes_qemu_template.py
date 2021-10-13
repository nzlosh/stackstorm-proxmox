from lib.base import ProxmoxAction


class NodesQemuTemplateAction(ProxmoxAction):
    """
    Create a Template.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
