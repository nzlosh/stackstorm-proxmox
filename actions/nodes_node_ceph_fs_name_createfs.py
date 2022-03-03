import json
from packlib.base import ProxmoxAction


class NodesNodeCephFsNameCreatefsAction(ProxmoxAction):
    """
    Create a Ceph filesystem
    """

    def run(self, node, add_storage=False, name="cephfs", pg_num=128, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["add-storage", add_storage, "boolean"],
            ["name", name, "string"],
            ["node", node, "string"],
            ["pg_num", pg_num, "integer"],
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

        return self.proxmox.post(f"nodes/{node}/ceph/fs/{name}", **proxmox_kwargs)
