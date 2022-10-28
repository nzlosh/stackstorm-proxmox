import json
from packlib.base import ProxmoxAction


class ClusterOptionsSetOptionsAction(ProxmoxAction):
    """
    Set datacenter options.
    """

    def run(self, bwlimit=None, console=None, delete=None, description=None, email_from=None, fencing="watchdog", ha=None, http_proxy=None, keyboard=None, language=None, mac_prefix=None, max_workers=None, migration=None, migration_unsecure=None, next_id=None, u2f=None, webauthn=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "string"],
            ["console", console, "string"],
            ["delete", delete, "string"],
            ["description", description, "string"],
            ["email_from", email_from, "string"],
            ["fencing", fencing, "string"],
            ["ha", ha, "string"],
            ["http_proxy", http_proxy, "string"],
            ["keyboard", keyboard, "string"],
            ["language", language, "string"],
            ["mac_prefix", mac_prefix, "string"],
            ["max_workers", max_workers, "integer"],
            ["migration", migration, "string"],
            ["migration_unsecure", migration_unsecure, "boolean"],
            ["next-id", next_id, "string"],
            ["u2f", u2f, "string"],
            ["webauthn", webauthn, "string"],
            
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

        return self.proxmox.put(
            f"cluster/options",
            **proxmox_kwargs
        )
        