import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidCloneCloneVmAction(ProxmoxAction):
    """
    Create a copy of virtual machine/template.
    """

    def run(
        self,
        newid,
        node,
        vmid,
        bwlimit=0,
        description=None,
        prox_format=None,
        full=None,
        name=None,
        pool=None,
        snapname=None,
        storage=None,
        target=None,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["bwlimit", bwlimit, "integer"],
            ["description", description, "string"],
            ["format", prox_format, "string"],
            ["full", full, "boolean"],
            ["name", name, "string"],
            ["newid", newid, "integer"],
            ["node", node, "string"],
            ["pool", pool, "string"],
            ["snapname", snapname, "string"],
            ["storage", storage, "string"],
            ["target", target, "string"],
            ["vmid", vmid, "integer"],
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

        return self.proxmox.post(f"nodes/{node}/qemu/{vmid}/clone", **proxmox_kwargs)
