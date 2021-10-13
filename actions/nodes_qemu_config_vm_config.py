from lib.base import ProxmoxAction


class NodesQemuConfigVmConfigAction(ProxmoxAction):
    """
    Get the virtual machine configuration with pending configuration changes applied. Set the 'current' parameter to get the current configuration instead.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
