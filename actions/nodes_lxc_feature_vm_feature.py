from lib.base import ProxmoxAction


class NodesLxcFeatureVmFeatureAction(ProxmoxAction):
    """
    Check if feature for virtual machine is available.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
