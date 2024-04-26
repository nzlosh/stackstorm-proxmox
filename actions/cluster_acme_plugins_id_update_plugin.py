import json
from packlib.base import ProxmoxAction


class ClusterAcmePluginsIdUpdatePluginAction(ProxmoxAction):
    """
    Update ACME plugin configuration.
    """

    def run(
        self,
        prox_id,
        api=None,
        data=None,
        delete=None,
        digest=None,
        disable=None,
        nodes=None,
        validation_delay=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["api", api, "string"],
            ["data", data, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["disable", disable, "boolean"],
            ["id", prox_id, "string"],
            ["nodes", nodes, "string"],
            ["validation-delay", validation_delay, "integer"],
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

        return self.proxmox.put(f"cluster/acme/plugins/{id}", **proxmox_kwargs)
