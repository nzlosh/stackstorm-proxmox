import json
from packlib.base import ProxmoxAction


class AccessTfaUseridIdUpdateTfaEntryAction(ProxmoxAction):
    """
    Add a TFA entry for a user.
    """

    def run(
        self,
        prox_id,
        userid,
        description=None,
        enable=None,
        password=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["description", description, "string"],
            ["enable", enable, "boolean"],
            ["id", prox_id, "string"],
            ["password", password, "string"],
            ["userid", userid, "string"],
        ]:
            if api_arg[1] is None:
                continue
            if "[n]" in api_arg[0]:
                unit_list = json.loads(api_arg[1])
                for i, v in enumerate(unit_list):
                    proxmox_kwargs[api_arg[0].replace("[n]", str(i))] = v
            else:
                if api_arg[2] == "boolean":
                    api_arg[1] = int(api_arg[1])
                proxmox_kwargs[api_arg[0]] = api_arg[1]

        return self.proxmox.put(f"access/tfa/{userid}/{id}", **proxmox_kwargs)
