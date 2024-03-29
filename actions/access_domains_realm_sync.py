import json
from packlib.base import ProxmoxAction


class AccessDomainsRealmSyncAction(ProxmoxAction):
    """
    Syncs users and/or groups from the configured LDAP to user.cfg. NOTE: Synced groups will have the name 'name-$realm', so make sure those groups do not exist to prevent overwriting.
    """

    def run(self, enable_new, full, purge, realm, remove_vanished, scope, dry_run=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["dry-run", dry_run, "boolean"],
            ["enable-new", enable_new, "boolean"],
            ["full", full, "boolean"],
            ["purge", purge, "boolean"],
            ["realm", realm, "string"],
            ["remove-vanished", remove_vanished, "string"],
            ["scope", scope, "string"],
            
        ]:
            if api_arg[1] is None:
                continue
            if '[n]' in api_arg[0]:
                unit_list = json.loads(api_arg[1])
                for i, v in enumerate(unit_list):
                    proxmox_kwargs[api_arg[0].replace("[n]", str(i))] = v
            else:
                if api_arg[2] == "boolean":
                    api_arg[1] = int(api_arg[1])
                proxmox_kwargs[api_arg[0]] = api_arg[1]

        return self.proxmox.post(
            f"access/domains/{realm}/sync",
            **proxmox_kwargs
        )
        