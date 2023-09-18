import json
from packlib.base import ProxmoxAction


class NodesNodeCephPoolsCreatepoolAction(ProxmoxAction):
    """
    Create POOL
    """

    def run(self, name, node, add_storages=None, application=None, crush_rule=None, min_size=None, pg_autoscale_mode=None, pg_num=None, pg_num_min=None, size=None, target_size=None, target_size_ratio=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["add_storages", add_storages, "boolean"],
            ["application", application, "string"],
            ["crush_rule", crush_rule, "string"],
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
        