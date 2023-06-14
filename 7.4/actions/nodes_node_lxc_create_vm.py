import json
from packlib.base import ProxmoxAction


class NodesNodeLxcCreateVmAction(ProxmoxAction):
    """
    Create or restore a container.
    """

    def run(self, node, ostemplate, vmid, arch="amd64", bwlimit=0, cmode="tty", console=True, cores=None, cpulimit=0, cpuunits=100, debug=False, description=None, features=None, force=None, hookscript=None, hostname=None, ignore_unpack_errors=None, lock=None, memory=512, mp_list=None, nameserver=None, net_list=None, onboot=False, ostype=None, password=None, pool=None, protection=False, restore=None, rootfs=None, searchdomain=None, ssh_public_keys=None, start=False, startup=None, storage="local", swap=512, tags=None, template=False, timezone=None, tty=2, unique=None, unprivileged=False, unused_list=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["arch", arch, "string"],
            ["bwlimit", bwlimit, "number"],
            ["cmode", cmode, "string"],
            ["console", console, "boolean"],
            ["cores", cores, "integer"],
            ["cpulimit", cpulimit, "number"],
            ["cpuunits", cpuunits, "integer"],
            ["debug", debug, "boolean"],
            ["description", description, "string"],
            ["features", features, "string"],
            ["force", force, "boolean"],
            ["hookscript", hookscript, "string"],
            ["hostname", hostname, "string"],
            ["ignore-unpack-errors", ignore_unpack_errors, "boolean"],
            ["lock", lock, "string"],
            ["memory", memory, "integer"],
            ["mp[n]", mp_list, "string"],
            ["nameserver", nameserver, "string"],
            ["net[n]", net_list, "string"],
            ["node", node, "string"],
            ["onboot", onboot, "boolean"],
            ["ostemplate", ostemplate, "string"],
            ["ostype", ostype, "string"],
            ["password", password, "string"],
            ["pool", pool, "string"],
            ["protection", protection, "boolean"],
            ["restore", restore, "boolean"],
            ["rootfs", rootfs, "string"],
            ["searchdomain", searchdomain, "string"],
            ["ssh-public-keys", ssh_public_keys, "string"],
            ["start", start, "boolean"],
            ["startup", startup, "string"],
            ["storage", storage, "string"],
            ["swap", swap, "integer"],
            ["tags", tags, "string"],
            ["template", template, "boolean"],
            ["timezone", timezone, "string"],
            ["tty", tty, "integer"],
            ["unique", unique, "boolean"],
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

        return self.proxmox.post(
            f"nodes/{node}/lxc",
            **proxmox_kwargs
        )
        