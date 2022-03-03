import json
from packlib.base import ProxmoxAction


class NodesNodeCephMonMonidCreatemonAction(ProxmoxAction):
    """
    Create Ceph Monitor and Manager
    """

    def run(self, node, mon_address=None, monid=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["mon-address", mon_address, "string"],
            ["monid", monid, "string"],
            ["node", node, "string"],
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

        return self.proxmox.post(f"nodes/{node}/ceph/mon/{monid}", **proxmox_kwargs)
