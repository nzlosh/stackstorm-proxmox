import json
from packlib.base import ProxmoxAction


class NodesNodeCephOsdCreateosdAction(ProxmoxAction):
    """
    Create OSD
    """

    def run(
        self,
        dev,
        node,
        crush_device_class=None,
        db_dev=None,
        db_dev_size=None,
        encrypted=None,
        wal_dev=None,
        wal_dev_size=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["crush-device-class", crush_device_class, "string"],
            ["db_dev", db_dev, "string"],
            ["db_dev_size", db_dev_size, "number"],
            ["dev", dev, "string"],
            ["encrypted", encrypted, "boolean"],
            ["node", node, "string"],
            ["wal_dev", wal_dev, "string"],
            ["wal_dev_size", wal_dev_size, "number"],
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

        return self.proxmox.post(f"nodes/{node}/ceph/osd", **proxmox_kwargs)
