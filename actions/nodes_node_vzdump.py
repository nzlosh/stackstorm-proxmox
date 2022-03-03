import json
from packlib.base import ProxmoxAction


class NodesNodeVzdumpAction(ProxmoxAction):
    """
    Create backup.
    """

    def run(
        self,
        prox_all=False,
        bwlimit=0,
        compress="0",
        dumpdir=None,
        exclude=None,
        exclude_path=None,
        ionice=7,
        lockwait=180,
        mailnotification="always",
        mailto=None,
        maxfiles=None,
        mode="snapshot",
        node=None,
        pigz=0,
        pool=None,
        prune_backups="keep-all=1",
        quiet=False,
        remove=True,
        script=None,
        stdexcludes=True,
        stdout=None,
        stop=False,
        stopwait=10,
        storage=None,
        tmpdir=None,
        vmid=None,
        zstd=1,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["all", prox_all, "boolean"],
            ["bwlimit", bwlimit, "integer"],
            ["compress", compress, "string"],
            ["dumpdir", dumpdir, "string"],
            ["exclude", exclude, "string"],
            ["exclude-path", exclude_path, "string"],
            ["ionice", ionice, "integer"],
            ["lockwait", lockwait, "integer"],
            ["mailnotification", mailnotification, "string"],
            ["mailto", mailto, "string"],
            ["maxfiles", maxfiles, "integer"],
            ["mode", mode, "string"],
            ["node", node, "string"],
            ["pigz", pigz, "integer"],
            ["pool", pool, "string"],
            ["prune-backups", prune_backups, "string"],
            ["quiet", quiet, "boolean"],
            ["remove", remove, "boolean"],
            ["script", script, "string"],
            ["stdexcludes", stdexcludes, "boolean"],
            ["stdout", stdout, "boolean"],
            ["stop", stop, "boolean"],
            ["stopwait", stopwait, "integer"],
            ["storage", storage, "string"],
            ["tmpdir", tmpdir, "string"],
            ["vmid", vmid, "string"],
            ["zstd", zstd, "integer"],
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

        return self.proxmox.post(f"nodes/{node}/vzdump", **proxmox_kwargs)
