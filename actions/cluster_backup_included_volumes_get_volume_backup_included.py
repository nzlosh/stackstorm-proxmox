from lib.base import ProxmoxAction


class ClusterBackupIncluded_volumesGetVolumeBackupIncludedAction(ProxmoxAction):
    """
    Returns included guests and the backup status of their disks. Optimized to be used in ExtJS tree views.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
