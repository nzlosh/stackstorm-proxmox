import json
from packlib.base import ProxmoxAction


class ClusterBackupIdUpdateJobAction(ProxmoxAction):
    """
    Update vzdump backup job definition.
    """

    def run(self, prox_id, starttime, prox_all=None, bwlimit=None, compress=None, delete=None, dow=None, dumpdir=None, enabled=None, exclude=None, exclude_path=None, ionice=None, lockwait=None, mailnotification=None, mailto=None, maxfiles=None, mode=None, node=None, pigz=None, pool=None, quiet=None, remove=None, script=None, size=None, stdexcludes=None, stop=None, stopwait=None, storage=None, tmpdir=None, vmid=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["all", prox_all, "boolean"],
            ["bwlimit", bwlimit, "integer"],
            ["compress", compress, "string"],
            ["delete", delete, "string"],
            ["dow", dow, "string"],
            ["dumpdir", dumpdir, "string"],
            ["enabled", enabled, "boolean"],
            ["exclude", exclude, "string"],
            ["exclude-path", exclude_path, "string"],
            ["id", prox_id, "string"],
            ["ionice", ionice, "integer"],
            ["lockwait", lockwait, "integer"],
            ["mailnotification", mailnotification, "string"],
            ["mailto", mailto, "string"],
            ["maxfiles", maxfiles, "integer"],
            ["mode", mode, "string"],
            ["node", node, "string"],
            ["pigz", pigz, "integer"],
            ["pool", pool, "string"],
            ["quiet", quiet, "boolean"],
            ["remove", remove, "boolean"],
            ["script", script, "string"],
            ["size", size, "integer"],
            ["starttime", starttime, "string"],
            ["stdexcludes", stdexcludes, "boolean"],
            ["stop", stop, "boolean"],
            ["stopwait", stopwait, "integer"],
            ["storage", storage, "string"],
            ["tmpdir", tmpdir, "string"],
            ["vmid", vmid, "string"],
            
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
            f"cluster/backup/{id}",
            **proxmox_kwargs
        )
        