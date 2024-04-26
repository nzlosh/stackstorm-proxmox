import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidStatusStopVmStopAction(ProxmoxAction):
    """
    Stop virtual machine. The qemu process will exit immediately. This is akin to pulling the power plug of a running computer and may damage the VM data.
    """

    def run(
        self,
        node,
        vmid,
        keepActive=None,
        migratedfrom=None,
        overrule_shutdown=None,
        skiplock=None,
        timeout=None,
        profile_name=None,
        api_timeout=5,
    ):
        super().run(profile_name, api_timeout=api_timeout)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["keepActive", keepActive, "boolean"],
            ["migratedfrom", migratedfrom, "string"],
            ["node", node, "string"],
            ["overrule-shutdown", overrule_shutdown, "boolean"],
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

        return self.proxmox.post(f"nodes/{node}/qemu/{vmid}/status/stop", **proxmox_kwargs)
