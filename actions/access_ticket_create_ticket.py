import json
from packlib.base import ProxmoxAction


class AccessTicketCreateTicketAction(ProxmoxAction):
    """
    Create or verify authentication ticket.
    """

    def run(
        self,
        password,
        username,
        new_format=None,
        otp=None,
        path=None,
        privs=None,
        realm=None,
        tfa_challenge=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["new-format", new_format, "boolean"],
            ["otp", otp, "string"],
            ["password", password, "string"],
            ["path", path, "string"],
            ["privs", privs, "string"],
            ["realm", realm, "string"],
            ["tfa-challenge", tfa_challenge, "string"],
            ["username", username, "string"],
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

        return self.proxmox.post(f"access/ticket", **proxmox_kwargs)
