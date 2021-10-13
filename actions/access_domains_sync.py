from lib.base import ProxmoxAction


class AccessDomainsSyncAction(ProxmoxAction):
    """
    Syncs users and/or groups from the configured LDAP to user.cfg. NOTE: Synced groups will have the name 'name-$realm', so make sure those groups do not exist to prevent overwriting.
    """

    def run(self, _):
        super().run(response_timeout)
        raise NotImplementedError
