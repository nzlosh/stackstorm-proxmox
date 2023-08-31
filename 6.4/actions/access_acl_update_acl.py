import json
from packlib.base import ProxmoxAction


class AccessAclUpdateAclAction(ProxmoxAction):
    """
    Update Access Control List (add or remove permissions).
    """

    def run(self, path, roles, delete=None, groups=None, propagate=None, tokens=None, users=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["delete", delete, "boolean"],
            ["groups", groups, "string"],
            ["path", path, "string"],
            ["propagate", propagate, "boolean"],
            ["roles", roles, "string"],
            ["tokens", tokens, "string"],
            ["users", users, "string"],
            
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
            f"access/acl",
            **proxmox_kwargs
        )
        