import json
from packlib.base import ProxmoxAction


class NodesNodeCephOsdCreateosdAction(ProxmoxAction):
    """
    Create OSD
    """

    def run(self, dev, node, db_dev=None, db_size=bluestore_block_db_size or 10% of OSD size, encrypted=False, wal_dev=None, wal_size=bluestore_block_wal_size or 1% of OSD size, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["db_dev", db_dev, "string"],
            ["db_size", db_size, "number"],
            ["dev", dev, "string"],
            ["encrypted", encrypted, "boolean"],
            ["node", node, "string"],
            ["wal_dev", wal_dev, "string"],
            ["wal_size", wal_size, "number"],
            
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
            f"nodes/{node}/ceph/osd",
            **proxmox_kwargs
        )
        