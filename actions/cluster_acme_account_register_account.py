import json
from packlib.base import ProxmoxAction


class ClusterAcmeAccountRegisterAccountAction(ProxmoxAction):
    """
    Register a new ACME account with CA.
    """

    def run(
        self,
        contact,
        directory="https://acme-v02.api.letsencrypt.org/directory",
        name="default",
        tos_url=None,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["contact", contact, "string"],
            ["directory", directory, "string"],
            ["name", name, "string"],
            ["tos_url", tos_url, "string"],
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

        return self.proxmox.post(f"cluster/acme/account", **proxmox_kwargs)
