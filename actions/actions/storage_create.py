import json
from packlib.base import ProxmoxAction


class StorageCreateAction(ProxmoxAction):
    """
    Create a new storage.
    """

    def run(self, storage, prox_type, authsupported=None, base=None, blocksize=None, bwlimit=None, comstar_hg=None, comstar_tg=None, content=None, datastore=None, disable=None, domain=None, encryption_key=None, export=None, fingerprint=None, prox_format=None, fuse=None, is_mountpoint=None, iscsiprovider=None, krbd=None, lio_tpg=None, master_pubkey=None, maxfiles=None, mkdir=None, monhost=None, mountpoint=None, namespace=None, nodes=None, nowritecache=None, options=None, password=None, path=None, pool=None, port=None, portal=None, prune_backups=None, redundancy=None, saferemove=None, saferemove_throughput=None, server=None, server2=None, share=None, shared=None, smbversion=None, sparse=None, subdir=None, tagged_only=None, target=None, thinpool=None, transport=None, username=None, vgname=None, volume=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["authsupported", authsupported, "string"],
            ["base", base, "string"],
            ["blocksize", blocksize, "string"],
            ["bwlimit", bwlimit, "string"],
            ["comstar_hg", comstar_hg, "string"],
            ["comstar_tg", comstar_tg, "string"],
            ["content", content, "string"],
            ["datastore", datastore, "string"],
            ["disable", disable, "boolean"],
            ["domain", domain, "string"],
            ["encryption-key", encryption_key, "string"],
            ["export", export, "string"],
            ["fingerprint", fingerprint, "string"],
            ["format", prox_format, "string"],
            ["fuse", fuse, "boolean"],
            ["is_mountpoint", is_mountpoint, "string"],
            ["iscsiprovider", iscsiprovider, "string"],
            ["krbd", krbd, "boolean"],
            ["lio_tpg", lio_tpg, "string"],
            ["master-pubkey", master_pubkey, "string"],
            ["maxfiles", maxfiles, "integer"],
            ["mkdir", mkdir, "boolean"],
            ["monhost", monhost, "string"],
            ["mountpoint", mountpoint, "string"],
            ["namespace", namespace, "string"],
            ["nodes", nodes, "string"],
            ["nowritecache", nowritecache, "boolean"],
            ["options", options, "string"],
            ["password", password, "string"],
            ["path", path, "string"],
            ["pool", pool, "string"],
            ["port", port, "integer"],
            ["portal", portal, "string"],
            ["prune-backups", prune_backups, "string"],
            ["redundancy", redundancy, "integer"],
            ["saferemove", saferemove, "boolean"],
            ["saferemove_throughput", saferemove_throughput, "string"],
            ["server", server, "string"],
            ["server2", server2, "string"],
            ["share", share, "string"],
            ["shared", shared, "boolean"],
            ["smbversion", smbversion, "string"],
            ["sparse", sparse, "boolean"],
            ["storage", storage, "string"],
            ["subdir", subdir, "string"],
            ["tagged_only", tagged_only, "boolean"],
            ["target", target, "string"],
            ["thinpool", thinpool, "string"],
            ["transport", transport, "string"],
            ["type", prox_type, "string"],
            ["username", username, "string"],
            ["vgname", vgname, "string"],
            ["volume", volume, "string"],
            
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
            f"storage",
            **proxmox_kwargs
        )
        