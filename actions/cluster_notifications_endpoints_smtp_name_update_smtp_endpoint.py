import json
from packlib.base import ProxmoxAction


class ClusterNotificationsEndpointsSmtpNameUpdateSmtpEndpointAction(ProxmoxAction):
    """
    Update existing smtp endpoint
    """

    def run(
        self,
        name,
        author=None,
        comment=None,
        delete=None,
        digest=None,
        disable=None,
        from_address=None,
        mailto=None,
        mailto_user=None,
        mode=None,
        password=None,
        port=None,
        server=None,
        username=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["author", author, "string"],
            ["comment", comment, "string"],
            ["delete", delete, "array"],
            ["digest", digest, "string"],
            ["disable", disable, "boolean"],
            ["from-address", from_address, "string"],
            ["mailto", mailto, "array"],
            ["mailto-user", mailto_user, "array"],
            ["mode", mode, "string"],
            ["name", name, "string"],
            ["password", password, "string"],
            ["port", port, "integer"],
            ["server", server, "string"],
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

        return self.proxmox.put(f"cluster/notifications/endpoints/smtp/{name}", **proxmox_kwargs)
