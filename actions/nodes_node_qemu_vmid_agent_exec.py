import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidAgentExecAction(ProxmoxAction):
    """
    Executes the given command in the vm via the guest-agent and returns an object with the pid.
    """

    def run(self, node, vmid, command=None, input_data=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["command", command, "string"],
            ["input-data", input_data, "string"],
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

        return self.proxmox.post(f"nodes/{node}/qemu/{vmid}/agent/exec", **proxmox_kwargs)
