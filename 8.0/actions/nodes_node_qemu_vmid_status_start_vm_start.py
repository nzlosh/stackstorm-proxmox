import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidStatusStartVmStartAction(ProxmoxAction):
    """
    Start virtual machine.
    """

    def run(self, node, vmid, force_cpu=None, machine=None, migratedfrom=None, migration_network=None, migration_type=None, skiplock=None, stateuri=None, targetstorage=None, timeout=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["force-cpu", force_cpu, "string"],
            ["machine", machine, "string"],
            ["migratedfrom", migratedfrom, "string"],
            ["migration_network", migration_network, "string"],
            ["migration_type", migration_type, "string"],
            ["node", node, "string"],
            ["skiplock", skiplock, "boolean"],
            ["stateuri", stateuri, "string"],
            ["targetstorage", targetstorage, "string"],
            ["timeout", timeout, "integer"],
            ["vmid", vmid, "integer"],
            
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
            f"nodes/{node}/qemu/{vmid}/status/start",
            **proxmox_kwargs
        )
        