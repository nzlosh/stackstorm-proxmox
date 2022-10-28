import json
from packlib.base import ProxmoxAction


class ClusterMetricsServerIdUpdateAction(ProxmoxAction):
    """
    Update metric server configuration.
    """

    def run(self, prox_id, port, server, api_path_prefix=None, bucket=None, delete=None, digest=None, disable=None, influxdbproto="udp", max_body_size=25000000, mtu=1500, organization=None, path=None, proto=None, timeout=1, token=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["api-path-prefix", api_path_prefix, "string"],
            ["bucket", bucket, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["disable", disable, "boolean"],
            ["id", prox_id, "string"],
            ["influxdbproto", influxdbproto, "string"],
            ["max-body-size", max_body_size, "integer"],
            ["mtu", mtu, "integer"],
            ["organization", organization, "string"],
            ["path", path, "string"],
            ["port", port, "integer"],
            ["proto", proto, "string"],
            ["server", server, "string"],
            ["timeout", timeout, "integer"],
            ["token", token, "string"],
            
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

        return self.proxmox.put(
            f"cluster/metrics/server/{id}",
            **proxmox_kwargs
        )
        