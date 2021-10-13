from lib.base import ProxmoxAction


class PoolsReadPoolAction(ProxmoxAction):
    """
    Get pool configuration.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
