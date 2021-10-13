from lib.base import ProxmoxAction


class ClusterBackup-infoNot-backed-upGetGuestsNotInBackupAction(ProxmoxAction):
    """
    Shows all guests which are not covered by any backup job.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
