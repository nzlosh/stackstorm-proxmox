import json
from packlib.base import ProxmoxAction


class ClusterMetricsServerIdCreateAction(ProxmoxAction):
    """
    Create a new external metric server config
    """

    def run(self, prox_id, port, server, prox_type, disable=None, mtu=1500, path=None, proto=None, timeout=1, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["disable", disable, "boolean"],
            ["id", prox_id, "string"],
            ["mtu", mtu, "integer"],
            ["path", path, "string"],
            ["port", port, "integer"],
            ["proto", proto, "string"],
            ["server", server, "string"],
            ["timeout", timeout, "integer"],
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

        return self.proxmox.post(
            f"cluster/metrics/server/{id}",
            **proxmox_kwargs
        )
        