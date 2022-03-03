import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidStatusShutdownVmShutdownAction(ProxmoxAction):
    """
    Shutdown virtual machine. This is similar to pressing the power button on a physical machine.This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown.
    """

    def run(
        self,
        node,
        vmid,
        forceStop=False,
        keepActive=False,
        skiplock=None,
        timeout=None,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["forceStop", forceStop, "boolean"],
            ["keepActive", keepActive, "boolean"],
            ["node", node, "string"],
            ["skiplock", skiplock, "boolean"],
            ["timeout", timeout, "integer"],
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

        return self.proxmox.post(f"nodes/{node}/qemu/{vmid}/status/shutdown", **proxmox_kwargs)
