from lib.base import ProxmoxAction


class PoolsDeletePoolAction(ProxmoxAction):
    """
    Delete pool.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
