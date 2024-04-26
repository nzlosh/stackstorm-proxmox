import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidConfigVmConfigAction(ProxmoxAction):
    """
    Get the virtual machine configuration with pending configuration changes applied. Set the 'current' parameter to get the current configuration instead.
    """

    def run(self, node, vmid, current=None, snapshot=None, profile_name=None, api_timeout=5):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["current", current, "boolean"],
            ["node", node, "string"],
            ["snapshot", snapshot, "string"],
            ["vmid", vmid, "integer"],
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

        return self.proxmox.get(f"nodes/{node}/qemu/{vmid}/config", **proxmox_kwargs)
