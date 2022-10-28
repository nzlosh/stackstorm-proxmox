import json
from packlib.base import ProxmoxAction


class AccessTfaUseridAddTfaEntryAction(ProxmoxAction):
    """
    Add a TFA entry for a user.
    """

    def run(self, prox_type, userid, challenge=None, description=None, password=None, totp=None, value=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["challenge", challenge, "string"],
            ["description", description, "string"],
            ["password", password, "string"],
            ["totp", totp, "string"],
            ["type", prox_type, "string"],
            ["userid", userid, "string"],
            ["value", value, "string"],
            
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
            f"access/tfa/{userid}",
            **proxmox_kwargs
        )
        