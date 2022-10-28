import json
from packlib.base import ProxmoxAction


class StorageStorageUpdateAction(ProxmoxAction):
    """
    Update storage configuration.
    """

    def run(self, storage, blocksize=None, bwlimit=None, comstar_hg=None, comstar_tg=None, content=None, data_pool=None, delete=None, digest=None, disable=None, domain=None, encryption_key=None, fingerprint=None, prox_format=None, fs_name=None, fuse=None, is_mountpoint="no", keyring=None, krbd=None, lio_tpg=None, master_pubkey=None, max_protected_backups=Unlimited for users with Datastore.Allocate privilege, 5 for other users, maxfiles=None, mkdir=True, monhost=None, mountpoint=None, namespace=None, nocow=False, nodes=None, nowritecache=None, options=None, password=None, pool=None, port=8007, preallocation="metadata", prune_backups=None, saferemove=None, saferemove_throughput=None, server=None, server2=None, shared=None, smbversion="default", sparse=None, subdir=None, tagged_only=None, transport=None, username=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["blocksize", blocksize, "string"],
            ["bwlimit", bwlimit, "string"],
            ["comstar_hg", comstar_hg, "string"],
            ["comstar_tg", comstar_tg, "string"],
            ["content", content, "string"],
            ["data-pool", data_pool, "string"],
            ["delete", delete, "string"],
            ["digest", digest, "string"],
            ["disable", disable, "boolean"],
            ["domain", domain, "string"],
            ["encryption-key", encryption_key, "string"],
            ["fingerprint", fingerprint, "string"],
            ["format", prox_format, "string"],
            ["fs-name", fs_name, "string"],
            ["fuse", fuse, "boolean"],
            ["is_mountpoint", is_mountpoint, "string"],
            ["keyring", keyring, "string"],
            ["krbd", krbd, "boolean"],
            ["lio_tpg", lio_tpg, "string"],
            ["master-pubkey", master_pubkey, "string"],
            ["max-protected-backups", max_protected_backups, "integer"],
            ["maxfiles", maxfiles, "integer"],
            ["mkdir", mkdir, "boolean"],
            ["monhost", monhost, "string"],
            ["mountpoint", mountpoint, "string"],
            ["namespace", namespace, "string"],
            ["nocow", nocow, "boolean"],
            ["nodes", nodes, "string"],
            ["nowritecache", nowritecache, "boolean"],
            ["options", options, "string"],
            ["password", password, "string"],
            ["pool", pool, "string"],
            ["port", port, "integer"],
            ["preallocation", preallocation, "string"],
            ["prune-backups", prune_backups, "string"],
            ["saferemove", saferemove, "boolean"],
            ["saferemove_throughput", saferemove_throughput, "string"],
            ["server", server, "string"],
            ["server2", server2, "string"],
            ["shared", shared, "boolean"],
            ["smbversion", smbversion, "string"],
            ["sparse", sparse, "boolean"],
            ["storage", storage, "string"],
            ["subdir", subdir, "string"],
            ["tagged_only", tagged_only, "boolean"],
            ["transport", transport, "string"],
            ["username", username, "string"],
            
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
            f"storage/{storage}",
            **proxmox_kwargs
        )
        