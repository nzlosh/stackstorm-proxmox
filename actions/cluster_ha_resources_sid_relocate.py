import json
from packlib.base import ProxmoxAction


class ClusterHaResourcesSidRelocateAction(ProxmoxAction):
    """
    Request resource relocatzion to another node. This stops the service on the old node, and restarts it on the target node.
    """

    def run(self, node, sid, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["node", node, "string"],
            ["sid", sid, "string"],
            
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
            f"cluster/ha/resources/{sid}/relocate",
            **proxmox_kwargs
        )
        