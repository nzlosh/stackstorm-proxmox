import json
from packlib.base import ProxmoxAction


class AccessOpenidLoginAction(ProxmoxAction):
    """
     Verify OpenID authorization code and create a ticket.
    """

    def run(self, code, redirect_url, state, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["code", code, "string"],
            ["redirect-url", redirect_url, "string"],
            ["state", state, "string"],
            
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
            f"access/openid/login",
            **proxmox_kwargs
        )
        