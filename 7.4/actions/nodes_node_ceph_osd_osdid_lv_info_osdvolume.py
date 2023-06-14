import json
from packlib.base import ProxmoxAction


class NodesNodeCephOsdOsdidLvInfoOsdvolumeAction(ProxmoxAction):
    """
    Get OSD volume details
    """

    def run(self, node, osdid, prox_type="block", profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["node", node, "string"],
            ["osdid", osdid, "integer"],
            ["type", prox_type, "string"],
            
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

        return self.proxmox.get(
            f"nodes/{node}/ceph/osd/{osdid}/lv-info",
            **proxmox_kwargs
        )
        