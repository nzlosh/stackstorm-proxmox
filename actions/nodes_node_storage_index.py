import json
from packlib.base import ProxmoxAction


class NodesNodeStorageIndexAction(ProxmoxAction):
    """
    Get status for all datastores.
    """

    def run(
        self,
        node,
        content=None,
        enabled=False,
        prox_format=False,
        storage=None,
        target=None,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["content", content, "string"],
            ["enabled", enabled, "boolean"],
            ["format", prox_format, "boolean"],
            ["node", node, "string"],
            ["storage", storage, "string"],
            ["target", target, "string"],
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

        return self.proxmox.get(f"nodes/{node}/storage", **proxmox_kwargs)
