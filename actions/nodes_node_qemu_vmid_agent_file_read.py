import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidAgentFileReadFileReadAction(ProxmoxAction):
    """
    Reads the given file via guest agent. Is limited to 16777216 bytes.
    """

    def run(self, file, node, vmid, profile_name=None, api_timeout=5):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["file", file, "string"],
            ["node", node, "string"],
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

        return self.proxmox.get(f"nodes/{node}/qemu/{vmid}/agent/file-read", **proxmox_kwargs)
