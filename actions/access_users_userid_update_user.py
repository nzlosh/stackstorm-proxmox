import json
from packlib.base import ProxmoxAction


class AccessUsersUseridUpdateUserAction(ProxmoxAction):
    """
    Update user configuration.
    """

    def run(self, userid, append=None, comment=None, email=None, enable=None, expire=None, firstname=None, groups=None, keys=None, lastname=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["append", append, "boolean"],
            ["comment", comment, "string"],
            ["email", email, "string"],
            ["enable", enable, "boolean"],
            ["expire", expire, "integer"],
            ["firstname", firstname, "string"],
            ["groups", groups, "string"],
            ["keys", keys, "string"],
            ["lastname", lastname, "string"],
            ["userid", userid, "string"],
            
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
            f"access/users/{userid}",
            **proxmox_kwargs
        )
        