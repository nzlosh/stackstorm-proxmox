from lib.base import ProxmoxAction


class NodesQemuFeatureVmFeatureAction(ProxmoxAction):
    """
    Check if feature for virtual machine is available.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
