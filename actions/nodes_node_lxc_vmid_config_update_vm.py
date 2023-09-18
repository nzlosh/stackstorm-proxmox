import json
from packlib.base import ProxmoxAction


class NodesNodeLxcVmidConfigUpdateVmAction(ProxmoxAction):
    """
    Set container options.
    """

    def run(self, node, vmid, arch=None, cmode=None, console=None, cores=None, cpulimit=None, cpuunits=None, delete=None, description=None, digest=None, features=None, hookscript=None, hostname=None, lock=None, memory=None, mp_list=None, nameserver=None, net_list=None, onboot=None, ostype=None, protection=None, revert=None, rootfs=None, searchdomain=None, startup=None, swap=None, tags=None, template=None, tty=None, unprivileged=None, unused_list=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["arch", arch, "string"],
            ["cmode", cmode, "string"],
            ["console", console, "boolean"],
            ["cores", cores, "integer"],
            ["cpulimit", cpulimit, "number"],
            ["cpuunits", cpuunits, "integer"],
            ["delete", delete, "string"],
            ["description", description, "string"],
            ["digest", digest, "string"],
            ["features", features, "string"],
            ["hookscript", hookscript, "string"],
            ["hostname", hostname, "string"],
            ["lock", lock, "string"],
            ["memory", memory, "integer"],
            ["mp[n]", mp_list, "string"],
            ["nameserver", nameserver, "string"],
            ["net[n]", net_list, "string"],
            ["node", node, "string"],
            ["onboot", onboot, "boolean"],
            ["ostype", ostype, "string"],
            ["protection", protection, "boolean"],
            ["revert", revert, "string"],
            ["rootfs", rootfs, "string"],
            ["searchdomain", searchdomain, "string"],
            ["startup", startup, "string"],
            ["swap", swap, "integer"],
            ["tags", tags, "string"],
            ["template", template, "boolean"],
            ["tty", tty, "integer"],
            ["unprivileged", unprivileged, "boolean"],
            ["unused[n]", unused_list, "string"],
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

        return self.proxmox.put(
            f"nodes/{node}/lxc/{vmid}/config",
            **proxmox_kwargs
        )
        