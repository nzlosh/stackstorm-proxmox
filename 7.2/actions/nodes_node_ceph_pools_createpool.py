import json
from packlib.base import ProxmoxAction


class NodesNodeCephPoolsCreatepoolAction(ProxmoxAction):
    """
    Create Ceph pool
    """

    def run(self, name, node, add_storages=True, application="rbd", crush_rule=None, erasure_coding=None, min_size=2, pg_autoscale_mode="warn", pg_num=128, pg_num_min=None, size=3, target_size=None, target_size_ratio=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["add_storages", add_storages, "boolean"],
            ["application", application, "string"],
            ["crush_rule", crush_rule, "string"],
            ["erasure-coding", erasure_coding, "string"],
            ["min_size", min_size, "integer"],
            ["name", name, "string"],
            ["node", node, "string"],
            ["pg_autoscale_mode", pg_autoscale_mode, "string"],
            ["pg_num", pg_num, "integer"],
            ["pg_num_min", pg_num_min, "integer"],
            ["size", size, "integer"],
            ["target_size", target_size, "string"],
            ["target_size_ratio", target_size_ratio, "number"],
            
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
            f"nodes/{node}/ceph/pools",
            **proxmox_kwargs
        )
        