# proxmox integration pack

> StackStorm integration for Proxmox APIv2.
Carlos <nzlosh@yahoo.com>

### Contributors


## Configuration

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `default_profile` | string | True |  | The default profile to use in actions when none is given. |
| `profiles` | array | True |  | A profile describing environment and credentials require to establish a connection. |
## Actions


The pack provides the following actions:

### nodes_qemu_resize_resize_vm
_Extend volume size._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disk` | string | True | False | _The disk you want to resize._ |
| `node` | string | True | False | _The cluster node name._ |
| `size` | string | True | False | _The new size. With the `+` sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_sdn_ipams_read
_Read sdn ipam configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `ipam` | string | True | False | _The SDN ipam object identifier._ |
### nodes_apt_repositories
_Get APT repository information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_spiceshell
_Creates a SPICE shell._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cmd` | string | False | False | _Run specific command or default to login._ |
| `cmd_opts` | string | False | False | _Add parameters to a command. Encoded as null terminated strings._ |
| `node` | string | True | False | _The cluster node name._ |
| `proxy` | string | False | False | _SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI)._ |
### cluster_sdn_controllers_delete
_Delete sdn controller object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `controller` | string | True | False | _The SDN controller object identifier._ |
### cluster_log
_Read cluster log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `max` | integer | False | False | _Maximum number of entries._ |
### cluster_acme_challenge-schema_challengeschema
_Get schema of ACME challenge types._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_qemu_status_start_vm_start
_Start virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force_cpu` | string | False | False | _Override QEMU's -cpu argument with the given string._ |
| `machine` | string | False | False | _Specifies the Qemu machine type._ |
| `migratedfrom` | string | False | False | _The cluster node name._ |
| `migration_network` | string | False | False | _CIDR of the (sub) network that is used for migration._ |
| `migration_type` | string | False | False | _Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance._ |
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `stateuri` | string | False | False | _Some command save/restore state from this location._ |
| `targetstorage` | string | False | False | _Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself._ |
| `timeout` | integer | False | False | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_ceph_pools_setpool
_Change POOL settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `application` | string | False | False | _The application of the pool._ |
| `crush_rule` | string | False | False | _The rule to use for mapping object placement in the cluster._ |
| `min_size` | integer | False | False | _Minimum number of replicas per object_ |
| `name` | string | True | False | _The name of the pool. It must be unique._ |
| `node` | string | True | False | _The cluster node name._ |
| `pg_autoscale_mode` | string | False | False | _The automatic PG scaling mode of the pool._ |
| `pg_num` | integer | False | False | _Number of placement groups._ |
| `pg_num_min` | integer | False | False | _Minimal number of placement groups._ |
| `size` | integer | False | False | _Number of replicas per object_ |
| `target_size` | string | False | False | _The estimated target size of the pool for the PG autoscaler._ |
| `target_size_ratio` | number | False | False | _The estimated target ratio of the pool for the PG autoscaler._ |
### cluster_sdn_dns_delete
_Delete sdn dns object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns` | string | True | False | _The SDN dns object identifier._ |
### cluster_config_totem
_Get corosync totem protocol settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### cluster_firewall_macros_get_macros
_List available macros_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_replication_status_job_status
_Get replication job status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `node` | string | True | False | _The cluster node name._ |
### access_openid_auth-url_auth_url
_Get the OpenId Authorization Url for the specified realm._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `realm` | string | True | False | _Authentication domain ID_ |
| `redirect_url` | string | True | False | _Redirection Url. The client should set this to the used server url (location.origin)._ |
### nodes_qemu_firewall_options_get_options
_Get VM firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_backup_included_volumes_get_volume_backup_included
_Returns included guests and the backup status of their disks. Optimized to be used in ExtJS tree views._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _The job ID._ |
### nodes_qemu_move_disk_move_vm_disk
_Move volume to different storage._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | integer | False | False | _Override I/O bandwidth limit (in KiB/s)._ |
| `delete` | boolean | False | False | _Delete the original disk after successful copy. By default the original disk is kept as unused disk._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disk` | string | True | False | _The disk you want to move._ |
| `format` | string | False | False | _Target Format._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _Target storage._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_users_tfa_read_user_tfa_type
_Get user TFA types (Personal and Realm)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `userid` | string | True | False | _User ID_ |
### nodes_lxc_config_vm_config
_Get container configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `current` | boolean | False | False | _Get current values (instead of pending values)._ |
| `node` | string | True | False | _The cluster node name._ |
| `snapshot` | string | False | False | _Fetch config values from given snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_metrics_server_delete
_Remove Metric server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Description unavailable._ |
### nodes_qemu_unlink
_Unlink/delete disk images._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called 'unused[n]', which contains the volume ID. Unlink of unused[n] always cause physical removal._ |
| `idlist` | string | True | False | _A list of disk IDs you want to delete._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_set-user-password
_Sets the password for the given user to the given password_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `crypted` | boolean | False | False | _set to 1 if the password has already been passed through crypt()_ |
| `node` | string | True | False | _The cluster node name._ |
| `password` | string | True | True | _The new password._ |
| `username` | string | True | False | _The user to set the password for._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_apt_update_list_updates
_List available updates._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_agent_ping
_Execute ping._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_users_token_read_token
_Get specific API token information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `tokenid` | string | True | False | _User-specific token identifier._ |
| `userid` | string | True | False | _User ID_ |
### nodes_qemu_clone_clone_vm
_Create a copy of virtual machine/template._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | integer | False | False | _Override I/O bandwidth limit (in KiB/s)._ |
| `description` | string | False | False | _Description for the new VM._ |
| `format` | string | False | False | _Target format for file storage. Only valid for full clone._ |
| `full` | boolean | False | False | _Create a full copy of all disks. This is always done when you clone a normal VM. For VM templates, we try to create a linked clone by default._ |
| `name` | string | False | False | _Set a name for the new VM._ |
| `newid` | integer | True | False | _VMID for the clone._ |
| `node` | string | True | False | _The cluster node name._ |
| `pool` | string | False | False | _Add the new VM to the specified pool._ |
| `snapname` | string | False | False | _The name of the snapshot._ |
| `storage` | string | False | False | _Target storage for full clone._ |
| `target` | string | False | False | _Target node. Only allowed if the original VM is on shared storage._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_acl_update_acl
_Update Access Control List (add or remove permissions)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | boolean | False | False | _Remove permissions (instead of adding it)._ |
| `groups` | string | False | False | _List of groups._ |
| `path` | string | True | False | _Access control path_ |
| `propagate` | boolean | False | False | _Allow to propagate (inherit) permissions._ |
| `roles` | string | True | False | _List of roles._ |
| `tokens` | string | False | False | _List of API tokens._ |
| `users` | string | False | False | _List of users._ |
### nodes_scan_lvm_lvmscan
_List local LVM volume groups._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_disks_lvmthin_create
_Create an LVM thinpool_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | False | _Configure storage using the thinpool._ |
| `device` | string | True | False | _The block device you want to create the thinpool on._ |
| `name` | string | True | False | _The storage identifier._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_agent_get-fsinfo
_Execute get-fsinfo._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_resize_resize_vm
_Resize a container mount point._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disk` | string | True | False | _The disk you want to resize._ |
| `node` | string | True | False | _The cluster node name._ |
| `size` | string | True | False | _The new size. With the '+' sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_get-users
_Execute get-users._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_replication_schedule_now
_Schedule replication job to start as soon as possible._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_agent_exec-status
_Gets the status of the given pid started by the guest-agent_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `pid` | integer | True | False | _The PID to query_ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_services_start_service_start
_Start service._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | True | False | _Service ID_ |
### cluster_ha_resources_relocate
_Request resource relocatzion to another node. This stops the service on the old node, and restarts it on the target node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _Target node._ |
| `sid` | string | True | False | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
### cluster_config_join_join_info
_Get information needed to join this cluster over the connected node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | False | False | _The node for which the joinee gets the nodeinfo. _ |
### cluster_ceph_metadata
_Get ceph metadata._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `scope` | string | False | False | _Description unavailable._ |
### nodes_qemu_config_vm_config
_Get the virtual machine configuration with pending configuration changes applied. Set the 'current' parameter to get the current configuration instead._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `current` | boolean | False | False | _Get current values (instead of pending values)._ |
| `node` | string | True | False | _The cluster node name._ |
| `snapshot` | string | False | False | _Fetch config values from given snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_firewall_aliases_read_alias
_Read alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _Alias name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_migrate_migrate_vm_precondition
_Get preconditions for migration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `target` | string | False | False | _Target node._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_config_apiversion_join_api_version
_Return the version of the cluster join API available on this node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_dns_update_dns
_Write DNS settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns1` | string | False | False | _First name server IP address._ |
| `dns2` | string | False | False | _Second name server IP address._ |
| `dns3` | string | False | False | _Third name server IP address._ |
| `node` | string | True | False | _The cluster node name._ |
| `search` | string | True | False | _Search domain for host-name lookup._ |
### cluster_firewall_ipset_remove_ip
_Remove IP or Network from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _IP set name._ |
### nodes_qemu_status_stop_vm_stop
_Stop virtual machine. The qemu process will exit immediately. Thisis akin to pulling the power plug of a running computer and may damage the VM data_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `keepActive` | boolean | False | False | _Do not deactivate storage volumes._ |
| `migratedfrom` | string | False | False | _The cluster node name._ |
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `timeout` | integer | False | False | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_shutdown
_Execute shutdown._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_storage_file-restore_list
_List files and directories for single file restore under the given path._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `filepath` | string | True | False | _base64-path to the directory or file being listed, or "/"._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
| `volume` | string | True | False | _Backup volume ID or name. Currently only PBS snapshots are supported._ |
### nodes_lxc_move_volume
_Move a rootfs-/mp-volume to a different storage_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | number | False | False | _Override I/O bandwidth limit (in KiB/s)._ |
| `delete` | boolean | False | False | _Delete the original volume after successful copy. By default the original is kept as an unused volume entry._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _Target Storage._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `volume` | string | True | False | _Volume which will be moved._ |
### nodes_config_set_options
_Set node configuration options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acme` | string | False | False | _Node specific ACME settings._ |
| `acmedomain[n]` | string | False | False | _ACME domain and validation plugin_ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `description` | string | False | False | _Description for the Node. Shown in the web-interface node notes panel. This is saved as comment inside the configuration file._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | False | _The cluster node name._ |
| `startall_onboot_delay` | integer | False | False | _Initial delay in seconds, before starting all the Virtual Guests with on-boot enabled._ |
| `wakeonlan` | string | False | False | _MAC address for wake on LAN_ |
### nodes_hosts_get_etc_hosts
_Get the content of /etc/hosts._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_firewall_refs
_Lists possible IPSet/Alias reference which are allowed in source/dest properties._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `type` | string | False | False | _Only list references of specified type._ |
### cluster_sdn_controllers_read
_Read sdn controller configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `controller` | string | True | False | _The SDN controller object identifier._ |
| `pending` | boolean | False | False | _Display pending config._ |
| `running` | boolean | False | False | _Display running config._ |
### nodes_aplinfo
_Get list of appliances._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_pools_destroypool
_Destroy pool_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _If true, destroys pool even if in use_ |
| `name` | string | True | False | _The name of the pool. It must be unique._ |
| `node` | string | True | False | _The cluster node name._ |
| `remove_storages` | boolean | False | False | _Remove all pveceph-managed storages configured for this pool_ |
### nodes_apt_update_update_database
_This is used to resynchronize the package index files from their sources (apt-get update)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `notify` | boolean | False | False | _Send notification mail about new packages (to email address specified for user 'root@pam')._ |
| `quiet` | boolean | False | False | _Only produces output suitable for logging, omitting progress indicators._ |
### cluster_firewall_aliases_update_alias
_Update IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `comment` | string | False | False | _Description unavailable._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _Alias name._ |
| `rename` | string | False | False | _Rename an existing alias._ |
### nodes_tasks_log_read_task_log
_Read task log._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `start` | integer | False | False | _Description unavailable._ |
| `upid` | string | True | False | _Description unavailable._ |
### nodes_dns
_Read DNS settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_lxc_firewall_rules_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_get-osinfo
_Execute get-osinfo._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_status_node_cmd
_Reboot or shutdown a node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | True | False | _Specify the command._ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_sdn_zones_delete
_Delete sdn zone object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `zone` | string | True | False | _The SDN zone object identifier._ |
### nodes_subscription_delete
_Delete subscription key of this node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_lxc_pending_vm_pending
_Get container configuration, including pending changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### pools_update_pool
_Update pool data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | False | _Description unavailable._ |
| `delete` | boolean | False | False | _Remove vms/storage (instead of adding it)._ |
| `poolid` | string | True | False | _Description unavailable._ |
| `storage` | string | False | False | _List of storage IDs._ |
| `vms` | string | False | False | _List of virtual machines._ |
### cluster_firewall_rules_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | False | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | False | _Descriptive comment._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dest` | string | False | False | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | False | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | False | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | False | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | False | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | False | _Log level for firewall rule._ |
| `macro` | string | False | False | _Use predefined standard macro._ |
| `moveto` | integer | False | False | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `proto` | string | False | False | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | False | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | False | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `type` | string | False | False | _Rule type._ |
### nodes_ceph_osd_out
_ceph osd out_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `osdid` | integer | True | False | _OSD ID_ |
### nodes_vzdump_defaults
_Get the currently configured vzdump defaults._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | False | False | _The storage identifier._ |
### nodes_disks_wipedisk_wipe_disk
_Wipe a disk or partition._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | True | False | _Block device name_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_lxc_status_current_vm_status
_Get virtual machine status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_clone_clone_vm
_Create a container clone/copy_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | number | False | False | _Override I/O bandwidth limit (in KiB/s)._ |
| `description` | string | False | False | _Description for the new CT._ |
| `full` | boolean | False | False | _Create a full copy of all disks. This is always done when you clone a normal CT. For CT templates, we try to create a linked clone by default._ |
| `hostname` | string | False | False | _Set a hostname for the new CT._ |
| `newid` | integer | True | False | _VMID for the clone._ |
| `node` | string | True | False | _The cluster node name._ |
| `pool` | string | False | False | _Add the new CT to the specified pool._ |
| `snapname` | string | False | False | _The name of the snapshot._ |
| `storage` | string | False | False | _Target storage for full clone._ |
| `target` | string | False | False | _Target node. Only allowed if the original VM is on shared storage._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_config_get_config
_Get node configuration options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `property` | string | False | False | _Return only a specific property from the node configuration._ |
### nodes_apt_changelog
_Get package changelogs._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _Package name._ |
| `node` | string | True | False | _The cluster node name._ |
| `version` | string | False | False | _Package version._ |
### nodes_qemu_agent_get-timezone
_Execute get-timezone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_hardware_pci_mdev_mdevscan
_List mediated device types for given PCI device._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `pciid` | string | True | False | _The PCI ID to list the mdev types for._ |
### cluster_nextid
_Get next free VMID. If you pass an VMID it will raise an error if the ID is already used._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `vmid` | integer | False | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_file-write
_Writes the given file via guest agent._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `content` | string | True | False | _The content to write into the file._ |
| `file` | string | True | False | _The path to the file._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_subscription_update
_Update subscription info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _Always connect to server, even if we have up to date info inside local cache._ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `ebtables` | boolean | False | False | _Enable ebtables rules cluster wide._ |
| `enable` | integer | False | False | _Enable or disable the firewall cluster wide._ |
| `log_ratelimit` | string | False | False | _Log ratelimiting settings_ |
| `policy_in` | string | False | False | _Input policy._ |
| `policy_out` | string | False | False | _Output policy._ |
### storage_read
_Read storage configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `storage` | string | True | False | _The storage identifier._ |
### cluster_sdn_controllers_update
_Update sdn controller object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `asn` | integer | False | False | _autonomous system number_ |
| `controller` | string | True | False | _The SDN controller object identifier._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `ebgp` | boolean | False | False | _Enable ebgp. (remote-as external)_ |
| `ebgp_multihop` | integer | False | False | _Description unavailable._ |
| `loopback` | string | False | False | _source loopback interface._ |
| `node` | string | False | False | _The cluster node name._ |
| `peers` | string | False | False | _peers address list._ |
### cluster_firewall_options_get_options
_Get Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_qemu_agent_network-get-interfaces
_Execute network-get-interfaces._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_spiceproxy
_Returns a SPICE configuration to connect to the VM._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `proxy` | string | False | False | _SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI)._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_ceph_rules
_List ceph rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_time
_Read server time and time zone settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `enable` | boolean | False | False | _Enable host firewall rules._ |
| `log_level_in` | string | False | False | _Log level for incoming traffic._ |
| `log_level_out` | string | False | False | _Log level for outgoing traffic._ |
| `log_nf_conntrack` | boolean | False | False | _Enable logging of conntrack information._ |
| `ndp` | boolean | False | False | _Enable NDP (Neighbor Discovery Protocol)._ |
| `nf_conntrack_allow_invalid` | boolean | False | False | _Allow invalid packets on connection tracking._ |
| `nf_conntrack_max` | integer | False | False | _Maximum number of tracked connections._ |
| `nf_conntrack_tcp_timeout_established` | integer | False | False | _Conntrack established timeout._ |
| `nf_conntrack_tcp_timeout_syn_recv` | integer | False | False | _Conntrack syn recv timeout._ |
| `node` | string | True | False | _The cluster node name._ |
| `nosmurfs` | boolean | False | False | _Enable SMURFS filter._ |
| `protection_synflood` | boolean | False | False | _Enable synflood protection_ |
| `protection_synflood_burst` | integer | False | False | _Synflood protection rate burst by ip src._ |
| `protection_synflood_rate` | integer | False | False | _Synflood protection rate syn/sec by ip src._ |
| `smurf_log_level` | string | False | False | _Log level for SMURFS filter._ |
| `tcp_flags_log_level` | string | False | False | _Log level for illegal tcp flags filter._ |
| `tcpflags` | boolean | False | False | _Filter illegal combinations of TCP flags._ |
### cluster_sdn_vnets_subnets_delete
_Delete sdn subnet object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `subnet` | string | True | False | _The SDN subnet object identifier._ |
| `vnet` | string | True | False | _The SDN vnet object identifier._ |
### nodes_qemu_status_reset_vm_reset
_Reset virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_status_suspend_vm_suspend
_Suspend the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_get-time
_Execute get-time._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_roles_update_role
_Update an existing role._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `append` | boolean | False | False | _Description unavailable._ |
| `privs` | string | False | False | _Description unavailable._ |
| `roleid` | string | True | False | _Description unavailable._ |
### nodes_storage_download-url_download_url
_Download templates and ISO images by using an URL._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `checksum` | string | False | False | _The expected checksum of the file._ |
| `checksum_algorithm` | string | False | False | _The algorithm to calculate the checksum of the file._ |
| `content` | string | True | False | _Content type._ |
| `filename` | string | True | False | _The name of the file to create. Caution: This will be normalized!_ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
| `url` | string | True | False | _The URL to download the file from._ |
| `verify_certificates` | boolean | False | False | _If false, no SSL/TLS certificates will be verified._ |
### nodes_apt_repositories_change_repository
_Change the properties of a repository. Currently only allows enabling/disabling._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Digest to detect modifications._ |
| `enabled` | boolean | False | False | _Whether the repository should be enabled or not._ |
| `index` | integer | True | False | _Index within the file (starting from 0)._ |
| `node` | string | True | False | _The cluster node name._ |
| `path` | string | True | False | _Path to the containing file._ |
### nodes_ceph_restart
_Restart ceph services._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | False | False | _Ceph service name._ |
### nodes_qemu_agent_suspend-disk
_Execute suspend-disk._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_storage_content_updateattributes
_Update volume attributes_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `notes` | string | False | False | _The new notes._ |
| `storage` | string | False | False | _The storage identifier._ |
| `volume` | string | True | False | _Volume identifier_ |
### nodes_qemu_migrate_migrate_vm
_Migrate virtual machine. Creates a new migration task._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | integer | False | False | _Override I/O bandwidth limit (in KiB/s)._ |
| `force` | boolean | False | False | _Allow to migrate VMs which use local devices. Only root may use this option._ |
| `migration_network` | string | False | False | _CIDR of the (sub) network that is used for migration._ |
| `migration_type` | string | False | False | _Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance._ |
| `node` | string | True | False | _The cluster node name._ |
| `online` | boolean | False | False | _Use online/live migration if VM is running. Ignored if VM is stopped._ |
| `target` | string | True | False | _Target node._ |
| `targetstorage` | string | False | False | _Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `with_local_disks` | boolean | False | False | _Enable live storage migration for local disk_ |
### nodes_qemu_agent_get-vcpus
_Execute get-vcpus._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_config_nodes_addnode
_Adds a node to the cluster configuration. This call is for internal use._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `apiversion` | integer | False | False | _The JOIN_API_VERSION of the new node._ |
| `force` | boolean | False | False | _Do not throw error if node already exists._ |
| `link[n]` | string | False | False | _Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)_ |
| `new_node_ip` | string | False | False | _IP Address of node to add. Used as fallback if no links are given._ |
| `node` | string | True | False | _The cluster node name._ |
| `nodeid` | integer | False | False | _Node id for this node._ |
| `votes` | integer | False | False | _Number of votes for this node_ |
### nodes_netstat
_Read tap/vm network device interface counters_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_capabilities_qemu_cpu_index
_List all custom and default CPU models._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_lxc_status_resume_vm_resume
_Resume the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_get-memory-block-info
_Execute get-memory-block-info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_disks_smart
_Get SMART Health of a disk._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | True | False | _Block device name_ |
| `healthonly` | boolean | False | False | _If true returns only the health status_ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_backup-info_not-backed-up_get_guests_not_in_backup
_Shows all guests which are not covered by any backup job._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_qemu_firewall_aliases_update_alias
_Update IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `comment` | string | False | False | _Description unavailable._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _Alias name._ |
| `node` | string | True | False | _The cluster node name._ |
| `rename` | string | False | False | _Rename an existing alias._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_migrate_migrate_vm
_Migrate the container to another node. Creates a new migration task._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | number | False | False | _Override I/O bandwidth limit (in KiB/s)._ |
| `node` | string | True | False | _The cluster node name._ |
| `online` | boolean | False | False | _Use online/live migration._ |
| `restart` | boolean | False | False | _Use restart migration_ |
| `target` | string | True | False | _Target node._ |
| `timeout` | integer | False | False | _Timeout in seconds for shutdown for restart migration_ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_tfa_change_tfa
_Change user u2f authentication._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | False | _The action to perform_ |
| `config` | string | False | False | _A TFA configuration. This must currently be of type TOTP of not set at all._ |
| `key` | string | False | True | _When adding TOTP, the shared secret value._ |
| `password` | string | False | True | _The current password._ |
| `response` | string | False | False | _Either the the response to the current u2f registration challenge, or, when adding TOTP, the currently valid TOTP value._ |
| `userid` | string | True | False | _User ID_ |
### storage_update
_Update storage configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `blocksize` | string | False | False | _block size_ |
| `bwlimit` | string | False | False | _Set bandwidth/io limits various operations._ |
| `comstar_hg` | string | False | False | _host group for comstar views_ |
| `comstar_tg` | string | False | False | _target group for comstar views_ |
| `content` | string | False | False | _Allowed content types.

NOTE: the value 'rootdir' is used for Containers, and value 'images' for VMs.
_ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | False | _Flag to disable the storage._ |
| `domain` | string | False | False | _CIFS domain._ |
| `encryption_key` | string | False | False | _Encryption key. Use 'autogen' to generate one automatically without passphrase._ |
| `fingerprint` | string | False | False | _Certificate SHA 256 fingerprint._ |
| `format` | string | False | False | _Default image format._ |
| `fuse` | boolean | False | False | _Mount CephFS through FUSE._ |
| `is_mountpoint` | string | False | False | _Assume the given path is an externally managed mountpoint and consider the storage offline if it is not mounted. Using a boolean (yes/no) value serves as a shortcut to using the target path in this field._ |
| `krbd` | boolean | False | False | _Always access rbd through krbd kernel module._ |
| `lio_tpg` | string | False | False | _target portal group for Linux LIO targets_ |
| `master_pubkey` | string | False | False | _Base64-encoded, PEM-formatted public RSA key. Used to encrypt a copy of the encryption-key which will be added to each encrypted backup._ |
| `maxfiles` | integer | False | False | _Deprecated: use 'prune-backups' instead. Maximal number of backup files per VM. Use '0' for unlimited._ |
| `mkdir` | boolean | False | False | _Create the directory if it doesn't exist._ |
| `monhost` | string | False | False | _IP addresses of monitors (for external clusters)._ |
| `mountpoint` | string | False | False | _mount point_ |
| `namespace` | string | False | False | _RBD Namespace._ |
| `nocow` | boolean | False | False | _Set the NOCOW flag on files. Disables data checksumming and causes data errors to be unrecoverable from while allowing direct I/O. Only use this if data does not need to be any more safe than on a single ext4 formatted disk with no underlying raid system._ |
| `nodes` | string | False | False | _List of cluster node names._ |
| `nowritecache` | boolean | False | False | _disable write caching on the target_ |
| `options` | string | False | False | _NFS mount options (see 'man nfs')_ |
| `password` | string | False | True | _Password for accessing the share/datastore._ |
| `pool` | string | False | False | _Pool._ |
| `port` | integer | False | False | _For non default port._ |
| `prune_backups` | string | False | False | _The retention options with shorter intervals are processed first with --keep-last being the very first one. Each option covers a specific period of time. We say that backups within this period are covered by this option. The next option does not take care of already covered backups and only considers older backups._ |
| `saferemove` | boolean | False | False | _Zero-out data when removing LVs._ |
| `saferemove_throughput` | string | False | False | _Wipe throughput (cstream -t parameter value)._ |
| `server` | string | False | False | _Server IP or DNS name._ |
| `server2` | string | False | False | _Backup volfile server IP or DNS name._ |
| `shared` | boolean | False | False | _Mark storage as shared._ |
| `smbversion` | string | False | False | _SMB protocol version_ |
| `sparse` | boolean | False | False | _use sparse volumes_ |
| `storage` | string | True | False | _The storage identifier._ |
| `subdir` | string | False | False | _Subdir to mount._ |
| `tagged_only` | boolean | False | False | _Only use logical volumes tagged with 'pve-vm-ID'._ |
| `transport` | string | False | False | _Gluster transport: tcp or rdma_ |
| `username` | string | False | False | _RBD Id._ |
### nodes_qemu_config_update_vm
_Set virtual machine options (synchrounous API) - You should consider using the POST method instead for any actions involving hotplug or storage allocation._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acpi` | boolean | False | False | _Enable/disable ACPI._ |
| `agent` | string | False | False | _Enable/disable Qemu GuestAgent and its properties._ |
| `arch` | string | False | False | _Virtual processor architecture. Defaults to the host._ |
| `args` | string | False | False | _Arbitrary arguments passed to kvm._ |
| `audio0` | string | False | False | _Configure a audio device, useful in combination with QXL/Spice._ |
| `autostart` | boolean | False | False | _Automatic restart after crash (currently ignored)._ |
| `balloon` | integer | False | False | _Amount of target RAM for the VM in MB. Using zero disables the ballon driver._ |
| `bios` | string | False | False | _Select BIOS implementation._ |
| `boot` | string | False | False | _Specify guest boot order. Use with 'order=', usage with no key or 'legacy=' is deprecated._ |
| `bootdisk` | string | False | False | _Enable booting from specified disk. Deprecated: Use 'boot: order=foo;bar' instead._ |
| `cdrom` | string | False | False | _This is an alias for option -ide2_ |
| `cicustom` | string | False | False | _cloud-init: Specify custom files to replace the automatically generated ones at start._ |
| `cipassword` | string | False | False | _cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords._ |
| `citype` | string | False | False | _Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows._ |
| `ciuser` | string | False | False | _cloud-init: User name to change ssh keys and password for instead of the image's configured default user._ |
| `cores` | integer | False | False | _The number of cores per socket._ |
| `cpu` | string | False | False | _Emulated CPU type._ |
| `cpulimit` | number | False | False | _Limit of CPU usage._ |
| `cpuunits` | integer | False | False | _CPU weight for a VM._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `description` | string | False | False | _Description for the VM. Shown in the web-interface VM's summary. This is saved as comment inside the configuration file._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `efidisk0` | string | False | False | _Configure a Disk for storing EFI vars. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume. Note that SIZE_IN_GiB is ignored here and that the default EFI vars are copied to the volume instead._ |
| `force` | boolean | False | False | _Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called 'unused[n]', which contains the volume ID. Unlink of unused[n] always cause physical removal._ |
| `freeze` | boolean | False | False | _Freeze CPU at startup (use 'c' monitor command to start execution)._ |
| `hookscript` | string | False | False | _Script that will be executed during various steps in the vms lifetime._ |
| `hostpci[n]` | string | False | False | _Map host PCI devices into guest._ |
| `hotplug` | string | False | False | _Selectively enable hotplug features. This is a comma separated list of hotplug features: 'network', 'disk', 'cpu', 'memory' and 'usb'. Use '0' to disable hotplug completely. Value '1' is an alias for the default 'network,disk,usb'._ |
| `hugepages` | string | False | False | _Enable/disable hugepages memory._ |
| `ide[n]` | string | False | False | _Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `ipconfig[n]` | string | False | False | _cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string 'dhcp' can be used for IP addresses to use DHCP, in which case no explicit
gateway should be provided.
For IPv6 the special string 'auto' can be used to use stateless autoconfiguration. This requires
cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using
dhcp on IPv4.
_ |
| `ivshmem` | string | False | False | _Inter-VM shared memory. Useful for direct communication between VMs, or to the host._ |
| `keephugepages` | boolean | False | False | _Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts._ |
| `keyboard` | string | False | False | _Keybord layout for vnc server. Default is read from the '/etc/pve/datacenter.cfg' configuration file.It should not be necessary to set it._ |
| `kvm` | boolean | False | False | _Enable/disable KVM hardware virtualization._ |
| `localtime` | boolean | False | False | _Set the real time clock to local time. This is enabled by default if ostype indicates a Microsoft OS._ |
| `lock` | string | False | False | _Lock/unlock the VM._ |
| `machine` | string | False | False | _Specifies the Qemu machine type._ |
| `memory` | integer | False | False | _Amount of RAM for the VM in MB. This is the maximum available memory when you use the balloon device._ |
| `migrate_downtime` | number | False | False | _Set maximum tolerated downtime (in seconds) for migrations._ |
| `migrate_speed` | integer | False | False | _Set maximum speed (in MB/s) for migrations. Value 0 is no limit._ |
| `name` | string | False | False | _Set a name for the VM. Only used on the configuration web interface._ |
| `nameserver` | string | False | False | _cloud-init: Sets DNS server IP address for a container. Create will'
	    .' automatically use the setting from the host if neither searchdomain nor nameserver'
	    .' are set._ |
| `net[n]` | string | False | False | _Specify network devices._ |
| `node` | string | True | False | _The cluster node name._ |
| `numa` | boolean | False | False | _Enable/disable NUMA._ |
| `numa[n]` | string | False | False | _NUMA topology._ |
| `onboot` | boolean | False | False | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | False | _Specify guest operating system._ |
| `parallel[n]` | string | False | False | _Map host parallel devices (n is 0 to 2)._ |
| `protection` | boolean | False | False | _Sets the protection flag of the VM. This will disable the remove VM and remove disk operations._ |
| `reboot` | boolean | False | False | _Allow reboot. If set to '0' the VM exit on reboot._ |
| `revert` | string | False | False | _Revert a pending change._ |
| `rng0` | string | False | False | _Configure a VirtIO-based Random Number Generator._ |
| `sata[n]` | string | False | False | _Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsi[n]` | string | False | False | _Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsihw` | string | False | False | _SCSI controller model_ |
| `searchdomain` | string | False | False | _cloud-init: Sets DNS search domains for a container. Create will'
	    .' automatically use the setting from the host if neither searchdomain nor nameserver'
	    .' are set._ |
| `serial[n]` | string | False | False | _Create a serial device inside the VM (n is 0 to 3)_ |
| `shares` | integer | False | False | _Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `smbios1` | string | False | False | _Specify SMBIOS type 1 fields._ |
| `smp` | integer | False | False | _The number of CPUs. Please use option -sockets instead._ |
| `sockets` | integer | False | False | _The number of CPU sockets._ |
| `spice_enhancements` | string | False | False | _Configure additional enhancements for SPICE._ |
| `sshkeys` | string | False | False | _cloud-init: Setup public SSH keys (one key per line, OpenSSH format)._ |
| `startdate` | string | False | False | _Set the initial date of the real time clock. Valid format for date are:'now' or '2006-06-17T16:01:21' or '2006-06-17'._ |
| `startup` | string | False | False | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `tablet` | boolean | False | False | _Enable/disable the USB tablet device._ |
| `tags` | string | False | False | _Tags of the VM. This is only meta information._ |
| `tdf` | boolean | False | False | _Enable/disable time drift fix._ |
| `template` | boolean | False | False | _Enable/disable Template._ |
| `unused[n]` | string | False | False | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `usb[n]` | string | False | False | _Configure an USB device (n is 0 to 4)._ |
| `vcpus` | integer | False | False | _Number of hotplugged vcpus._ |
| `vga` | string | False | False | _Configure the VGA hardware._ |
| `virtio[n]` | string | False | False | _Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `vmgenid` | string | False | False | _Set VM Generation ID. Use '1' to autogenerate on create or update, pass '0' to disable explicitly._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `vmstatestorage` | string | False | False | _Default storage for VM state volumes/files._ |
| `watchdog` | string | False | False | _Create a virtual hardware watchdog device._ |
### version
_API version details. The result also includes the global datacenter confguration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_ceph_mgr_createmgr
_Create Ceph Manager_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | False | False | _The ID for the manager, when omitted the same as the nodename_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_configdb
_Get Ceph configuration database._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_subscription_set
_Set subscription key._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | True | _Proxmox VE subscription key_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_pending_vm_pending
_Get the virtual machine configuration with both current and pending values._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_firewall_ipset_read_ip
_Read IP or Network settings from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `name` | string | True | False | _IP set name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_acme_account_deactivate_account
_Deactivate existing ACME account at CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | False | False | _ACME account config file name._ |
### nodes_lxc_status_start_vm_start
_Start the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `debug` | boolean | False | False | _If set, enables very verbose debug log-level on start._ |
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_file-read
_Reads the given file via guest agent. Is limited to 16777216 bytes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `file` | string | True | False | _The path to the file_ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_groups_update_group
_Update group data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | False | _Description unavailable._ |
| `groupid` | string | True | False | _Description unavailable._ |
### nodes_network_network_config
_Read network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `iface` | string | True | False | _Network interface name._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_agent_get-memory-blocks
_Execute get-memory-blocks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_storage_upload
_Upload templates and ISO images._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `content` | string | True | False | _Content type._ |
| `filename` | string | True | False | _The name of the file to create._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
| `tmpfilename` | string | False | False | _The source file name. This parameter is usually set by the REST handler. You can only overwrite it when connecting to the trusted port on localhost._ |
### nodes_qemu_agent_get-host-name
_Execute get-host-name._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_scan_nfs_nfsscan
_Scan remote NFS server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `server` | string | True | False | _The server address (name or IP)._ |
### nodes_ceph_osd_scrub
_Instruct the OSD to scrub._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `deep` | boolean | False | False | _If set, instructs a deep scrub instead of a normal one._ |
| `node` | string | True | False | _The cluster node name._ |
| `osdid` | integer | True | False | _OSD ID_ |
### nodes_qemu_agent_info
_Execute info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_domains_sync
_Syncs users and/or groups from the configured LDAP to user.cfg. NOTE: Synced groups will have the name 'name-$realm', so make sure those groups do not exist to prevent overwriting._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dry_run` | boolean | False | False | _If set, does not write anything._ |
| `enable_new` | boolean | False | False | _Enable newly synced users immediately._ |
| `full` | boolean | False | False | _If set, uses the LDAP Directory as source of truth, deleting users or groups not returned from the sync. Otherwise only syncs information which is not already present, and does not deletes or modifies anything else._ |
| `purge` | boolean | False | False | _Remove ACLs for users or groups which were removed from the config during a sync._ |
| `realm` | string | True | False | _Authentication domain ID_ |
| `scope` | string | False | False | _Select what to sync._ |
### nodes_qemu_snapshot_rollback
_Rollback VM state to specified snapshot._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | True | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_termproxy
_Creates a TCP proxy connection._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_firewall_log
_Read firewall log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `start` | integer | False | False | _Description unavailable._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_firewall_log
_Read firewall log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `start` | integer | False | False | _Description unavailable._ |
### nodes_lxc_vncwebsocket
_Opens a weksocket for VNC traffic._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `port` | integer | True | False | _Port number returned by previous vncproxy call._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `vncticket` | string | True | False | _Ticket from previous call to vncproxy._ |
### nodes_hosts_write_etc_hosts
_Write /etc/hosts._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `data` | string | True | False | _The target content of /etc/hosts._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_monitor
_Execute Qemu monitor commands._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | True | False | _The monitor command._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_vncwebsocket
_Opens a websocket for VNC traffic._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `port` | integer | True | False | _Port number returned by previous vncproxy call._ |
| `vncticket` | string | True | False | _Ticket from previous call to vncproxy._ |
### nodes_firewall_options_get_options
_Get host firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_agent_fstrim
_Execute fstrim._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_sendkey_vm_sendkey
_Send key event to virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | True | _The key (qemu monitor encoding)._ |
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_replication_delete
_Mark replication job for removal._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _Will remove the jobconfig entry, but will not cleanup._ |
| `id` | string | True | False | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `keep` | boolean | False | False | _Keep replicated data at target (do not remove)._ |
### cluster_sdn_zones_update
_Update sdn zone object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bridge` | string | False | False | _Description unavailable._ |
| `controller` | string | False | False | _Frr router name_ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dns` | string | False | False | _dns api server_ |
| `dnszone` | string | False | False | _dns domain zone  ex: mydomain.com_ |
| `dp_id` | integer | False | False | _Faucet dataplane id_ |
| `exitnodes` | string | False | False | _List of cluster node names._ |
| `ipam` | string | False | False | _use a specific ipam_ |
| `mac` | string | False | False | _Anycast logical router mac address_ |
| `mtu` | integer | False | False | _MTU_ |
| `nodes` | string | False | False | _List of cluster node names._ |
| `peers` | string | False | False | _peers address list._ |
| `reversedns` | string | False | False | _reverse dns api server_ |
| `tag` | integer | False | False | _Service-VLAN Tag_ |
| `vlan_protocol` | string | False | False | _Description unavailable._ |
| `vrf_vxlan` | integer | False | False | _l3vni._ |
| `zone` | string | True | False | _The SDN zone object identifier._ |
### nodes_storage_content_copy
_Copy a volume. This is experimental code - do not use._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | False | False | _The storage identifier._ |
| `target` | string | True | False | _Target volume identifier_ |
| `target_node` | string | False | False | _Target node. Default is local node._ |
| `volume` | string | True | False | _Source volume identifier_ |
### nodes_disks_lvm_create
_Create an LVM Volume Group_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | False | _Configure storage using the Volume Group_ |
| `device` | string | True | False | _The block device you want to create the volume group on_ |
| `name` | string | True | False | _The storage identifier._ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_resources
_Resources index (cluster wide)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `type` | string | False | False | _Description unavailable._ |
### cluster_metrics_server_update
_Update metric server configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_path_prefix` | string | False | False | _An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy._ |
| `bucket` | string | False | False | _The InfluxDB bucket/db. Only necessary when using the http v2 api._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | False | _Flag to disable the plugin._ |
| `id` | string | True | False | _The ID of the entry._ |
| `influxdbproto` | string | False | False | _Description unavailable._ |
| `max_body_size` | integer | False | False | _InfluxDB max-body-size in bytes. Requests are batched up to this size._ |
| `mtu` | integer | False | False | _MTU for metrics transmission over UDP_ |
| `organization` | string | False | False | _The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api._ |
| `path` | string | False | False | _root graphite path (ex: proxmox.mycluster.mykey)_ |
| `port` | integer | True | False | _server network port_ |
| `proto` | string | False | False | _Protocol to send graphite data. TCP or UDP (default)_ |
| `server` | string | True | False | _server dns name or IP address_ |
| `timeout` | integer | False | False | _graphite TCP socket timeout (default=1)_ |
| `token` | string | False | False | _The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead._ |
### cluster_firewall_rules_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
### nodes_storage_content_info
_Get volume attributes_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | False | False | _The storage identifier._ |
| `volume` | string | True | False | _Volume identifier_ |
### pools_delete_pool
_Delete pool._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `poolid` | string | True | False | _Description unavailable._ |
### nodes_ceph_start
_Start ceph services._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | False | False | _Ceph service name._ |
### nodes_sdn_zones_content_index
_List zone content._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `zone` | string | True | False | _The SDN zone object identifier._ |
### cluster_status_get_status
_Get cluster status information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### access_users_token_remove_token
_Remove API token for a specific user._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `tokenid` | string | True | False | _User-specific token identifier._ |
| `userid` | string | True | False | _User ID_ |
### cluster_acme_plugins_delete_plugin
_Delete ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Unique identifier for ACME plugin instance._ |
### nodes_lxc_firewall_rules_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_snapshot_rollback
_Rollback LXC state to specified snapshot._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | True | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_scan_iscsi_iscsiscan
_Scan remote iSCSI server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `portal` | string | True | False | _The iSCSI portal (IP or DNS name with optional port)._ |
### cluster_tasks
_List recent tasks (cluster wide)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_qemu_rrd
_Read VM RRD statistics (returns PNG)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `ds` | string | True | False | _The list of datasources you want to display._ |
| `node` | string | True | False | _The cluster node name._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_spiceproxy
_Returns a SPICE configuration to connect to the CT._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `proxy` | string | False | False | _SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI)._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_scan_zfs_zfsscan
_Scan zfs pool list on local node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_mon_destroymon
_Destroy Ceph Monitor and Manager._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `monid` | string | True | False | _Monitor ID_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_firewall_ipset_remove_ip
_Remove IP or Network from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _IP set name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_scan_lvmthin_lvmthinscan
_List local LVM Thin Pools._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vg` | string | True | False | _Description unavailable._ |
### pools_read_pool
_Get pool configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `poolid` | string | True | False | _Description unavailable._ |
### cluster_config_qdevice_status
_Get QDevice status_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_migrateall
_Migrate all VMs and Containers._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `maxworkers` | integer | False | False | _Maximal number of parallel migration job. If not set use 'max_workers' from datacenter.cfg, one of both must be set!_ |
| `node` | string | True | False | _The cluster node name._ |
| `target` | string | True | False | _Target node._ |
| `vms` | string | False | False | _Only consider Guests with these IDs._ |
| `with_local_disks` | boolean | False | False | _Enable live storage migration for local disk_ |
### nodes_qemu_firewall_rules_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_firewall_aliases_read_alias
_Read alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _Alias name._ |
### nodes_disks_directory_create
_Create a Filesystem on an unused disk. Will be mounted under '/mnt/pve/NAME'._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | False | _Configure storage using the directory._ |
| `device` | string | True | False | _The block device you want to create the filesystem on._ |
| `filesystem` | string | False | False | _The desired filesystem._ |
| `name` | string | True | False | _The storage identifier._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_status_resume_vm_resume
_Resume virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `nocheck` | boolean | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_sdn_vnets_subnets_read
_Read sdn subnet configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | False | _Display pending config._ |
| `running` | boolean | False | False | _Display running config._ |
| `subnet` | string | True | False | _The SDN subnet object identifier._ |
| `vnet` | string | True | False | _The SDN vnet object identifier._ |
### nodes_qemu_firewall_aliases_remove_alias
_Remove IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _Alias name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_permissions
_Retrieve effective permissions of given user/token._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `path` | string | False | False | _Only dump this specific path, not the whole tree._ |
| `userid` | string | False | False | _User ID or full API token ID_ |
### nodes_journal
_Read Journal_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `endcursor` | string | False | False | _End before the given Cursor. Conflicts with 'until'_ |
| `lastentries` | integer | False | False | _Limit to the last X lines. Conflicts with a range._ |
| `node` | string | True | False | _The cluster node name._ |
| `since` | integer | False | False | _Display all log since this UNIX epoch. Conflicts with 'startcursor'._ |
| `startcursor` | string | False | False | _Start after the given Cursor. Conflicts with 'since'_ |
| `until` | integer | False | False | _Display all log until this UNIX epoch. Conflicts with 'endcursor'._ |
### nodes_syslog
_Read system log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | False | False | _Service ID_ |
| `since` | string | False | False | _Display all log since this date-time string._ |
| `start` | integer | False | False | _Description unavailable._ |
| `until` | string | False | False | _Display all log until this date-time string._ |
### nodes_disks_lvmthin_index
_List LVM thinpools_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_termproxy
_Creates a VNC Shell proxy._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cmd` | string | False | False | _Run specific command or default to login._ |
| `cmd_opts` | string | False | False | _Add parameters to a command. Encoded as null terminated strings._ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_replication_update
_Update replication job configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | False | _Description._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | False | _Flag to disable/deactivate the entry._ |
| `id` | string | True | False | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `rate` | number | False | False | _Rate limit in mbps (megabytes per second) as floating point number._ |
| `remove_job` | string | False | False | _Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file._ |
| `schedule` | string | False | False | _Storage replication schedule. The format is a subset of `systemd` calendar events._ |
| `source` | string | False | False | _For internal use, to detect if the guest was stolen._ |
### nodes_qemu_template
_Create a Template._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | False | False | _If you want to convert only 1 disk to base image._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_disks_initgpt
_Initialize Disk with GPT_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | True | False | _Block device name_ |
| `node` | string | True | False | _The cluster node name._ |
| `uuid` | string | False | False | _UUID for the GPT table_ |
### cluster_firewall_groups_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | False | _Security Group name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
### nodes_network_update_network
_Update network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `address` | string | False | False | _IP address._ |
| `address6` | string | False | False | _IP address._ |
| `autostart` | boolean | False | False | _Automatically start interface on boot._ |
| `bond_primary` | string | False | False | _Specify the primary interface for active-backup bond._ |
| `bond_mode` | string | False | False | _Bonding mode._ |
| `bond_xmit_hash_policy` | string | False | False | _Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes._ |
| `bridge_ports` | string | False | False | _Specify the interfaces you want to add to your bridge._ |
| `bridge_vlan_aware` | boolean | False | False | _Enable bridge vlan support._ |
| `cidr` | string | False | False | _IPv4 CIDR._ |
| `cidr6` | string | False | False | _IPv6 CIDR._ |
| `comments` | string | False | False | _Comments_ |
| `comments6` | string | False | False | _Comments_ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `gateway` | string | False | False | _Default gateway address._ |
| `gateway6` | string | False | False | _Default ipv6 gateway address._ |
| `iface` | string | True | False | _Network interface name._ |
| `mtu` | integer | False | False | _MTU._ |
| `netmask` | string | False | False | _Network mask._ |
| `netmask6` | integer | False | False | _Network mask._ |
| `node` | string | True | False | _The cluster node name._ |
| `ovs_bonds` | string | False | False | _Specify the interfaces used by the bonding device._ |
| `ovs_bridge` | string | False | False | _The OVS bridge associated with a OVS port. This is required when you create an OVS port._ |
| `ovs_options` | string | False | False | _OVS interface options._ |
| `ovs_ports` | string | False | False | _Specify the interfaces you want to add to your bridge._ |
| `ovs_tag` | integer | False | False | _Specify a VLan tag (used by OVSPort, OVSIntPort, OVSBond)_ |
| `slaves` | string | False | False | _Specify the interfaces used by the bonding device._ |
| `type` | string | True | False | _Network interface type_ |
| `vlan_id` | integer | False | False | _vlan-id for a custom named vlan interface (ifupdown2 only)._ |
| `vlan_raw_device` | string | False | False | _Specify the raw interface for the vlan interface._ |
### cluster_replication_read
_Read replication job configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
### nodes_qemu_status_reboot_vm_reboot
_Reboot the VM by shutting it down, and starting it again. Applies pending changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `timeout` | integer | False | False | _Wait maximal timeout seconds for the shutdown._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_certificates_info
_Get information about node's certificates._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_firewall_ipset_update_ip
_Update IP or Network settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `comment` | string | False | False | _Description unavailable._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _IP set name._ |
| `nomatch` | boolean | False | False | _Description unavailable._ |
### nodes_qemu_rrddata
_Read VM RRD statistics_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `node` | string | True | False | _The cluster node name._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_firewall_rules_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | False | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | False | _Descriptive comment._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dest` | string | False | False | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | False | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | False | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | False | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | False | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | False | _Log level for firewall rule._ |
| `macro` | string | False | False | _Use predefined standard macro._ |
| `moveto` | integer | False | False | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `proto` | string | False | False | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | False | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | False | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `type` | string | False | False | _Rule type._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_firewall_rules_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_metrics_server_read
_Read metric server configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Description unavailable._ |
### cluster_firewall_rules_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pos` | integer | False | False | _Update rule at position <pos>._ |
### nodes_rrd
_Read node RRD statistics (returns PNG)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `ds` | string | True | False | _The list of datasources you want to display._ |
| `node` | string | True | False | _The cluster node name._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
### nodes_qemu_firewall_refs
_Lists possible IPSet/Alias reference which are allowed in source/dest properties._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `type` | string | False | False | _Only list references of specified type._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_config_join
_Joins this node into an existing cluster. If no links are given, default to IP resolved by node's hostname on single link (fallback fails for clusters with multiple links)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `fingerprint` | string | True | False | _Certificate SHA 256 fingerprint._ |
| `force` | boolean | False | False | _Do not throw error if node already exists._ |
| `hostname` | string | True | False | _Hostname (or IP) of an existing cluster member._ |
| `link[n]` | string | False | False | _Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)_ |
| `nodeid` | integer | False | False | _Node id for this node._ |
| `password` | string | True | True | _Superuser (root) password of peer node._ |
| `votes` | integer | False | False | _Number of votes for this node_ |
### nodes_execute
_Execute multiple commands in order._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `commands` | string | True | False | _JSON encoded array of commands._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_agent_suspend-hybrid
_Execute suspend-hybrid._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_users_token_update_token_info
_Update API token for a specific user._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | False | _Description unavailable._ |
| `expire` | integer | False | False | _API token expiration date (seconds since epoch). '0' means no expiration date._ |
| `privsep` | boolean | False | False | _Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user._ |
| `tokenid` | string | True | False | _User-specific token identifier._ |
| `userid` | string | True | False | _User ID_ |
### cluster_firewall_groups_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | False | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | False | _Descriptive comment._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dest` | string | False | False | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | False | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | False | _Flag to enable/disable a rule._ |
| `group` | string | True | False | _Security Group name._ |
| `icmp_type` | string | False | False | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | False | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | False | _Log level for firewall rule._ |
| `macro` | string | False | False | _Use predefined standard macro._ |
| `moveto` | integer | False | False | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `proto` | string | False | False | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | False | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | False | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `type` | string | False | False | _Rule type._ |
### nodes_qemu_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dhcp` | boolean | False | False | _Enable DHCP._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `enable` | boolean | False | False | _Enable/disable firewall rules._ |
| `ipfilter` | boolean | False | False | _Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added._ |
| `log_level_in` | string | False | False | _Log level for incoming traffic._ |
| `log_level_out` | string | False | False | _Log level for outgoing traffic._ |
| `macfilter` | boolean | False | False | _Enable/disable MAC address filter._ |
| `ndp` | boolean | False | False | _Enable NDP (Neighbor Discovery Protocol)._ |
| `node` | string | True | False | _The cluster node name._ |
| `policy_in` | string | False | False | _Input policy._ |
| `policy_out` | string | False | False | _Output policy._ |
| `radv` | boolean | False | False | _Allow sending Router Advertisement._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_version
_API version details_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_log
_Read ceph log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `start` | integer | False | False | _Description unavailable._ |
### cluster_acme_account_get_account
_Return existing ACME account information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | False | False | _ACME account config file name._ |
### nodes_qemu_snapshot_config_update_snapshot_config
_Update snapshot metadata._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `description` | string | False | False | _A textual description or comment._ |
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | True | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_ha_groups_delete
_Delete ha group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | False | _The HA group identifier._ |
### nodes_lxc_status_shutdown_vm_shutdown
_Shutdown the container. This will trigger a clean shutdown of the container, see lxc-stop(1) for details._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `forceStop` | boolean | False | False | _Make sure the Container stops._ |
| `node` | string | True | False | _The cluster node name._ |
| `timeout` | integer | False | False | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_firewall_ipset_read_ip
_Read IP or Network settings from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `name` | string | True | False | _IP set name._ |
### cluster_sdn_vnets_subnets_update
_Update sdn subnet object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dnszoneprefix` | string | False | False | _dns domain zone prefix  ex: 'adm' -> <hostname>.adm.mydomain.com_ |
| `gateway` | string | False | False | _Subnet Gateway: Will be assign on vnet for layer3 zones_ |
| `snat` | boolean | False | False | _enable masquerade for this subnet if pve-firewall_ |
| `subnet` | string | True | False | _The SDN subnet object identifier._ |
| `vnet` | string | False | False | _associated vnet_ |
### nodes_qemu_agent_suspend-ram
_Execute suspend-ram._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_agent_fsfreeze-status
_Execute fsfreeze-status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_config_update_vm_async
_Set virtual machine options (asynchrounous API)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acpi` | boolean | False | False | _Enable/disable ACPI._ |
| `agent` | string | False | False | _Enable/disable Qemu GuestAgent and its properties._ |
| `arch` | string | False | False | _Virtual processor architecture. Defaults to the host._ |
| `args` | string | False | False | _Arbitrary arguments passed to kvm._ |
| `audio0` | string | False | False | _Configure a audio device, useful in combination with QXL/Spice._ |
| `autostart` | boolean | False | False | _Automatic restart after crash (currently ignored)._ |
| `background_delay` | integer | False | False | _Time to wait for the task to finish. We return 'null' if the task finish within that time._ |
| `balloon` | integer | False | False | _Amount of target RAM for the VM in MB. Using zero disables the ballon driver._ |
| `bios` | string | False | False | _Select BIOS implementation._ |
| `boot` | string | False | False | _Specify guest boot order. Use with 'order=', usage with no key or 'legacy=' is deprecated._ |
| `bootdisk` | string | False | False | _Enable booting from specified disk. Deprecated: Use 'boot: order=foo;bar' instead._ |
| `cdrom` | string | False | False | _This is an alias for option -ide2_ |
| `cicustom` | string | False | False | _cloud-init: Specify custom files to replace the automatically generated ones at start._ |
| `cipassword` | string | False | False | _cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords._ |
| `citype` | string | False | False | _Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows._ |
| `ciuser` | string | False | False | _cloud-init: User name to change ssh keys and password for instead of the image's configured default user._ |
| `cores` | integer | False | False | _The number of cores per socket._ |
| `cpu` | string | False | False | _Emulated CPU type._ |
| `cpulimit` | number | False | False | _Limit of CPU usage._ |
| `cpuunits` | integer | False | False | _CPU weight for a VM._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `description` | string | False | False | _Description for the VM. Shown in the web-interface VM's summary. This is saved as comment inside the configuration file._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `efidisk0` | string | False | False | _Configure a Disk for storing EFI vars. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume. Note that SIZE_IN_GiB is ignored here and that the default EFI vars are copied to the volume instead._ |
| `force` | boolean | False | False | _Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called 'unused[n]', which contains the volume ID. Unlink of unused[n] always cause physical removal._ |
| `freeze` | boolean | False | False | _Freeze CPU at startup (use 'c' monitor command to start execution)._ |
| `hookscript` | string | False | False | _Script that will be executed during various steps in the vms lifetime._ |
| `hostpci[n]` | string | False | False | _Map host PCI devices into guest._ |
| `hotplug` | string | False | False | _Selectively enable hotplug features. This is a comma separated list of hotplug features: 'network', 'disk', 'cpu', 'memory' and 'usb'. Use '0' to disable hotplug completely. Value '1' is an alias for the default 'network,disk,usb'._ |
| `hugepages` | string | False | False | _Enable/disable hugepages memory._ |
| `ide[n]` | string | False | False | _Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `ipconfig[n]` | string | False | False | _cloud-init: Specify IP addresses and gateways for the corresponding interface.

IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.

The special string 'dhcp' can be used for IP addresses to use DHCP, in which case no explicit
gateway should be provided.
For IPv6 the special string 'auto' can be used to use stateless autoconfiguration. This requires
cloud-init 19.4 or newer.

If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using
dhcp on IPv4.
_ |
| `ivshmem` | string | False | False | _Inter-VM shared memory. Useful for direct communication between VMs, or to the host._ |
| `keephugepages` | boolean | False | False | _Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts._ |
| `keyboard` | string | False | False | _Keybord layout for vnc server. Default is read from the '/etc/pve/datacenter.cfg' configuration file.It should not be necessary to set it._ |
| `kvm` | boolean | False | False | _Enable/disable KVM hardware virtualization._ |
| `localtime` | boolean | False | False | _Set the real time clock to local time. This is enabled by default if ostype indicates a Microsoft OS._ |
| `lock` | string | False | False | _Lock/unlock the VM._ |
| `machine` | string | False | False | _Specifies the Qemu machine type._ |
| `memory` | integer | False | False | _Amount of RAM for the VM in MB. This is the maximum available memory when you use the balloon device._ |
| `migrate_downtime` | number | False | False | _Set maximum tolerated downtime (in seconds) for migrations._ |
| `migrate_speed` | integer | False | False | _Set maximum speed (in MB/s) for migrations. Value 0 is no limit._ |
| `name` | string | False | False | _Set a name for the VM. Only used on the configuration web interface._ |
| `nameserver` | string | False | False | _cloud-init: Sets DNS server IP address for a container. Create will'
	    .' automatically use the setting from the host if neither searchdomain nor nameserver'
	    .' are set._ |
| `net[n]` | string | False | False | _Specify network devices._ |
| `node` | string | True | False | _The cluster node name._ |
| `numa` | boolean | False | False | _Enable/disable NUMA._ |
| `numa[n]` | string | False | False | _NUMA topology._ |
| `onboot` | boolean | False | False | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | False | _Specify guest operating system._ |
| `parallel[n]` | string | False | False | _Map host parallel devices (n is 0 to 2)._ |
| `protection` | boolean | False | False | _Sets the protection flag of the VM. This will disable the remove VM and remove disk operations._ |
| `reboot` | boolean | False | False | _Allow reboot. If set to '0' the VM exit on reboot._ |
| `revert` | string | False | False | _Revert a pending change._ |
| `rng0` | string | False | False | _Configure a VirtIO-based Random Number Generator._ |
| `sata[n]` | string | False | False | _Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsi[n]` | string | False | False | _Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsihw` | string | False | False | _SCSI controller model_ |
| `searchdomain` | string | False | False | _cloud-init: Sets DNS search domains for a container. Create will'
	    .' automatically use the setting from the host if neither searchdomain nor nameserver'
	    .' are set._ |
| `serial[n]` | string | False | False | _Create a serial device inside the VM (n is 0 to 3)_ |
| `shares` | integer | False | False | _Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `smbios1` | string | False | False | _Specify SMBIOS type 1 fields._ |
| `smp` | integer | False | False | _The number of CPUs. Please use option -sockets instead._ |
| `sockets` | integer | False | False | _The number of CPU sockets._ |
| `spice_enhancements` | string | False | False | _Configure additional enhancements for SPICE._ |
| `sshkeys` | string | False | False | _cloud-init: Setup public SSH keys (one key per line, OpenSSH format)._ |
| `startdate` | string | False | False | _Set the initial date of the real time clock. Valid format for date are:'now' or '2006-06-17T16:01:21' or '2006-06-17'._ |
| `startup` | string | False | False | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `tablet` | boolean | False | False | _Enable/disable the USB tablet device._ |
| `tags` | string | False | False | _Tags of the VM. This is only meta information._ |
| `tdf` | boolean | False | False | _Enable/disable time drift fix._ |
| `template` | boolean | False | False | _Enable/disable Template._ |
| `unused[n]` | string | False | False | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `usb[n]` | string | False | False | _Configure an USB device (n is 0 to 4)._ |
| `vcpus` | integer | False | False | _Number of hotplugged vcpus._ |
| `vga` | string | False | False | _Configure the VGA hardware._ |
| `virtio[n]` | string | False | False | _Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `vmgenid` | string | False | False | _Set VM Generation ID. Use '1' to autogenerate on create or update, pass '0' to disable explicitly._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `vmstatestorage` | string | False | False | _Default storage for VM state volumes/files._ |
| `watchdog` | string | False | False | _Create a virtual hardware watchdog device._ |
### cluster_acme_tos_get_tos
_Retrieve ACME TermsOfService URL from CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `directory` | string | False | False | _URL of ACME CA directory endpoint._ |
### nodes_lxc_snapshot_config_get_snapshot_config
_Get snapshot configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | True | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_vncwebsocket
_Opens a weksocket for VNC traffic._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `port` | integer | True | False | _Port number returned by previous vncproxy call._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `vncticket` | string | True | False | _Ticket from previous call to vncproxy._ |
### cluster_options_set_options
_Set datacenter options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | string | False | False | _Set bandwidth/io limits various operations._ |
| `console` | string | False | False | _Select the default Console viewer. You can either use the builtin java applet (VNC; deprecated and maps to html5), an external virt-viewer comtatible application (SPICE), an HTML5 based vnc viewer (noVNC), or an HTML5 based console client (xtermjs). If the selected viewer is not available (e.g. SPICE not activated for the VM), the fallback is noVNC._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `email_from` | string | False | False | _Specify email address to send notification from (default is root@$hostname)_ |
| `fencing` | string | False | False | _Set the fencing mode of the HA cluster. Hardware mode needs a valid configuration of fence devices in /etc/pve/ha/fence.cfg. With both all two modes are used.

WARNING: 'hardware' and 'both' are EXPERIMENTAL & WIP_ |
| `ha` | string | False | False | _Cluster wide HA settings._ |
| `http_proxy` | string | False | False | _Specify external http proxy which is used for downloads (example: 'http://username:password@host:port/')_ |
| `keyboard` | string | False | False | _Default keybord layout for vnc server._ |
| `language` | string | False | False | _Default GUI language._ |
| `mac_prefix` | string | False | False | _Prefix for autogenerated MAC addresses._ |
| `max_workers` | integer | False | False | _Defines how many workers (per node) are maximal started  on actions like 'stopall VMs' or task from the ha-manager._ |
| `migration` | string | False | False | _For cluster wide migration settings._ |
| `migration_unsecure` | boolean | False | False | _Migration is secure using SSH tunnel by default. For secure private networks you can disable it to speed up migration. Deprecated, use the 'migration' property instead!_ |
| `u2f` | string | False | False | _u2f_ |
### nodes_rrddata
_Read node RRD statistics_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `node` | string | True | False | _The cluster node name._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
### nodes_qemu_firewall_log
_Read firewall log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `start` | integer | False | False | _Description unavailable._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_firewall_ipset_remove_ip
_Remove IP or Network from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _IP set name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_status_current_vm_status
_Get virtual machine status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_disks_directory_index
_PVE Managed Directory storages._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_pools_getpool
_List pool settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _The name of the pool. It must be unique._ |
| `node` | string | True | False | _The cluster node name._ |
| `verbose` | boolean | False | False | _If enabled, will display additional data(eg. statistics)._ |
### storage_delete
_Delete storage configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `storage` | string | True | False | _The storage identifier._ |
### nodes_qemu_vncproxy
_Creates a TCP VNC proxy connections._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `generate_password` | boolean | False | False | _Generates a random password to be used as ticket instead of the API ticket._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `websocket` | boolean | False | False | _starts websockify instead of vncproxy_ |
### cluster_ha_groups_read
_Read ha group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | False | _The HA group identifier._ |
### nodes_disks_zfs_detail
_Get details about a zpool._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _The storage identifier._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_scan_glusterfs_glusterfsscan
_Scan remote GlusterFS server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `server` | string | True | False | _The server address (name or IP)._ |
### nodes_qemu_feature_vm_feature
_Check if feature for virtual machine is available._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `feature` | string | True | False | _Feature to check._ |
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | False | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_firewall_aliases_update_alias
_Update IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `comment` | string | False | False | _Description unavailable._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _Alias name._ |
| `node` | string | True | False | _The cluster node name._ |
| `rename` | string | False | False | _Rename an existing alias._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_storage_content_delete
_Delete volume_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delay` | integer | False | False | _Time to wait for the task to finish. We return 'null' if the task finish within that time._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | False | False | _The storage identifier._ |
| `volume` | string | True | False | _Volume identifier_ |
### nodes_ceph_mds_createmds
_Create Ceph Metadata Server (MDS)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `hotstandby` | boolean | False | False | _Determines whether a ceph-mds daemon should poll and replay the log of an active MDS. Faster switch on MDS failure, but needs more idle resources._ |
| `name` | string | False | False | _The ID for the mds, when omitted the same as the nodename_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_lxc_snapshot_config_update_snapshot_config
_Update snapshot metadata._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `description` | string | False | False | _A textual description or comment._ |
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | True | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_time_set_timezone
_Set time zone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `timezone` | string | True | False | _Time zone. The file '/usr/share/zoneinfo/zone.tab' contains the list of valid names._ |
### nodes_qemu_agent_exec
_Executes the given command in the vm via the guest-agent and returns an object with the pid._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | False | False | _The command as a list of program + arguments_ |
| `input_data` | string | False | False | _Data to pass as 'input-data' to the guest. Usually treated as STDIN to 'command'._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_firewall_rules_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | False | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | False | _Descriptive comment._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dest` | string | False | False | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | False | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | False | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | False | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | False | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | False | _Log level for firewall rule._ |
| `macro` | string | False | False | _Use predefined standard macro._ |
| `moveto` | integer | False | False | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `proto` | string | False | False | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | False | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | False | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `type` | string | False | False | _Rule type._ |
### nodes_storage_prunebackups_dryrun
_Get prune information for backups. NOTE: this is only a preview and might not be what a subsequent prune call does if backups are removed/added in the meantime._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `prune_backups` | string | False | False | _Use these retention options instead of those from the storage configuration._ |
| `storage` | string | True | False | _The storage identifier._ |
| `type` | string | False | False | _Either 'qemu' or 'lxc'. Only consider backups for guests of this type._ |
| `vmid` | integer | False | False | _Only consider backups for this guest._ |
### nodes_certificates_custom_remove_custom_cert
_DELETE custom certificate chain and key._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `restart` | boolean | False | False | _Restart pveproxy._ |
### nodes_ceph_stop
_Stop ceph services._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | False | False | _Ceph service name._ |
### nodes_qemu_firewall_rules_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | False | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | False | _Descriptive comment._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dest` | string | False | False | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | False | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | False | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | False | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | False | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | False | _Log level for firewall rule._ |
| `macro` | string | False | False | _Use predefined standard macro._ |
| `moveto` | integer | False | False | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
| `proto` | string | False | False | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | False | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | False | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `type` | string | False | False | _Rule type._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_status_reboot_vm_reboot
_Reboot the container by shutting it down, and starting it again. Applies pending changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `timeout` | integer | False | False | _Wait maximal timeout seconds for the shutdown._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_acl_read_acl
_Get Access Control List (ACLs)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_qemu_status_shutdown_vm_shutdown
_Shutdown virtual machine. This is similar to pressing the power button on a physical machine.This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `forceStop` | boolean | False | False | _Make sure the VM stops._ |
| `keepActive` | boolean | False | False | _Do not deactivate storage volumes._ |
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `timeout` | integer | False | False | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_hardware_usb_usbscan
_List local USB devices._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_startall
_Start all VMs and containers located on this node (by default only those with onboot=1)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _Issue start command even if virtual guest have 'onboot' not set or set to off._ |
| `node` | string | True | False | _The cluster node name._ |
| `vms` | string | False | False | _Only consider guests from this comma separated list of VMIDs._ |
### nodes_tasks_status_read_task_status
_Read task status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `upid` | string | True | False | _Description unavailable._ |
### nodes_lxc_firewall_ipset_read_ip
_Read IP or Network settings from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `name` | string | True | False | _IP set name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_disks_list
_List local disks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `include_partitions` | boolean | False | False | _Also include partitions._ |
| `node` | string | True | False | _The cluster node name._ |
| `skipsmart` | boolean | False | False | _Skip smart checks._ |
| `type` | string | False | False | _Only list specific types of disks._ |
### nodes_scan_pbs_pbsscan
_Scan remote Proxmox Backup Server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `fingerprint` | string | False | False | _Certificate SHA 256 fingerprint._ |
| `node` | string | True | False | _The cluster node name._ |
| `password` | string | True | True | _User password or API token secret._ |
| `port` | integer | False | False | _Optional port._ |
| `server` | string | True | False | _The server address (name or IP)._ |
| `username` | string | True | False | _User-name or API token-ID._ |
### nodes_scan_cifs_cifsscan
_Scan remote CIFS server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `domain` | string | False | False | _SMB domain (Workgroup)._ |
| `node` | string | True | False | _The cluster node name._ |
| `password` | string | False | True | _User password._ |
| `server` | string | True | False | _The server address (name or IP)._ |
| `username` | string | False | False | _User name._ |
### nodes_network_delete_network
_Delete network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `iface` | string | True | False | _Network interface name._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_vzdump_extractconfig
_Extract configuration from vzdump backup archive._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `volume` | string | True | False | _Volume identifier_ |
### nodes_certificates_acme_certificate_revoke_certificate
_Revoke existing certificate from CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_status
_Get ceph status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_metrics_server_create
_Create a new external metric server config_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_path_prefix` | string | False | False | _An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy._ |
| `bucket` | string | False | False | _The InfluxDB bucket/db. Only necessary when using the http v2 api._ |
| `disable` | boolean | False | False | _Flag to disable the plugin._ |
| `id` | string | True | False | _The ID of the entry._ |
| `influxdbproto` | string | False | False | _Description unavailable._ |
| `max_body_size` | integer | False | False | _InfluxDB max-body-size in bytes. Requests are batched up to this size._ |
| `mtu` | integer | False | False | _MTU for metrics transmission over UDP_ |
| `organization` | string | False | False | _The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api._ |
| `path` | string | False | False | _root graphite path (ex: proxmox.mycluster.mykey)_ |
| `port` | integer | True | False | _server network port_ |
| `proto` | string | False | False | _Protocol to send graphite data. TCP or UDP (default)_ |
| `server` | string | True | False | _server dns name or IP address_ |
| `timeout` | integer | False | False | _graphite TCP socket timeout (default=1)_ |
| `token` | string | False | False | _The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead._ |
| `type` | string | True | False | _Plugin type._ |
### cluster_sdn_ipams_delete
_Delete sdn ipam object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `ipam` | string | True | False | _The SDN ipam object identifier._ |
### nodes_qemu_status_suspend_vm_suspend
_Suspend virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `statestorage` | string | False | False | _The storage for the VM state_ |
| `todisk` | boolean | False | False | _If set, suspends the VM to disk. Will be resumed on next VM start._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_qemu_firewall_ipset_update_ip
_Update IP or Network settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `comment` | string | False | False | _Description unavailable._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _IP set name._ |
| `node` | string | True | False | _The cluster node name._ |
| `nomatch` | boolean | False | False | _Description unavailable._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_ceph_crush
_Get OSD crush map_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_lxc_firewall_ipset_update_ip
_Update IP or Network settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | False | _Network/IP specification in CIDR format._ |
| `comment` | string | False | False | _Description unavailable._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _IP set name._ |
| `node` | string | True | False | _The cluster node name._ |
| `nomatch` | boolean | False | False | _Description unavailable._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_roles_read_role
_Get role configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `roleid` | string | True | False | _Description unavailable._ |
### cluster_ha_resources_migrate
_Request resource migration (online) to another node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _Target node._ |
| `sid` | string | True | False | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
### cluster_ha_groups_update
_Update ha group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | False | _Description._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `group` | string | True | False | _The HA group identifier._ |
| `nodes` | string | False | False | _List of cluster node names with optional priority._ |
| `nofailback` | boolean | False | False | _The CRM tries to run services on the node with the highest priority. If a node with higher priority comes online, the CRM migrates the service to that node. Enabling nofailback prevents that behavior._ |
| `restricted` | boolean | False | False | _Resources bound to restricted groups may only run on nodes defined by the group._ |
### access_ticket_get_ticket
_Dummy. Useful for formatters which want to provide a login page._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_storage_file-restore_download
_Extract a file or directory (as zip archive) from a PBS backup._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `filepath` | string | True | False | _base64-path to the directory or file to download._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
| `volume` | string | True | False | _Backup volume ID or name. Currently only PBS snapshots are supported._ |
### nodes_ceph_mgr_destroymgr
_Destroy Ceph Manager._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _The ID of the manager_ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_acme_plugins_get_plugin_config
_Get ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Unique identifier for ACME plugin instance._ |
### nodes_services_restart_service_restart
_Hard restart service. Use reload if you want to reduce interruptions._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | True | False | _Service ID_ |
### access_openid_login
_ Verify OpenID authorization code and create a ticket._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `code` | string | True | False | _OpenId authorization code._ |
| `redirect_url` | string | True | False | _Redirection Url. The client should set this to the used server url (location.origin)._ |
| `state` | string | True | False | _OpenId state._ |
### nodes_vncshell
_Creates a VNC Shell proxy._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cmd` | string | False | False | _Run specific command or default to login._ |
| `cmd_opts` | string | False | False | _Add parameters to a command. Encoded as null terminated strings._ |
| `height` | integer | False | False | _sets the height of the console in pixels._ |
| `node` | string | True | False | _The cluster node name._ |
| `websocket` | boolean | False | False | _use websocket instead of standard vnc._ |
| `width` | integer | False | False | _sets the width of the console in pixels._ |
### access_groups_read_group
_Get group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `groupid` | string | True | False | _Description unavailable._ |
### cluster_ha_status_manager_status
_Get full HA manger status, including LRM status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_ceph_config
_Get Ceph configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_acme_directories_get_directories
_Get named known ACME directory endpoints._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_report
_Gather various systems information about a node_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_firewall_aliases_remove_alias
_Remove IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _Alias name._ |
### nodes_firewall_rules_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
### nodes_lxc_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `dhcp` | boolean | False | False | _Enable DHCP._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `enable` | boolean | False | False | _Enable/disable firewall rules._ |
| `ipfilter` | boolean | False | False | _Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added._ |
| `log_level_in` | string | False | False | _Log level for incoming traffic._ |
| `log_level_out` | string | False | False | _Log level for outgoing traffic._ |
| `macfilter` | boolean | False | False | _Enable/disable MAC address filter._ |
| `ndp` | boolean | False | False | _Enable NDP (Neighbor Discovery Protocol)._ |
| `node` | string | True | False | _The cluster node name._ |
| `policy_in` | string | False | False | _Input policy._ |
| `policy_out` | string | False | False | _Output policy._ |
| `radv` | boolean | False | False | _Allow sending Router Advertisement._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_aplinfo_apl_download
_Download appliance templates._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage where the template will be stored_ |
| `template` | string | True | False | _The template which will downloaded_ |
### nodes_storage_rrddata
_Read storage RRD statistics._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
### access_ticket_create_ticket
_Create or verify authentication ticket._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `otp` | string | False | False | _One-time password for Two-factor authentication._ |
| `password` | string | True | True | _The secret password. This can also be a valid ticket._ |
| `path` | string | False | False | _Verify ticket, and check if user have access 'privs' on 'path'_ |
| `privs` | string | False | False | _Verify ticket, and check if user have access 'privs' on 'path'_ |
| `realm` | string | False | False | _You can optionally pass the realm using this parameter. Normally the realm is simply added to the username <username>@<relam>._ |
| `username` | string | True | False | _User name_ |
### nodes_lxc_config_update_vm
_Set container options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `arch` | string | False | False | _OS architecture type._ |
| `cmode` | string | False | False | _Console mode. By default, the console command tries to open a connection to one of the available tty devices. By setting cmode to 'console' it tries to attach to /dev/console instead. If you set cmode to 'shell', it simply invokes a shell inside the container (no login)._ |
| `console` | boolean | False | False | _Attach a console device (/dev/console) to the container._ |
| `cores` | integer | False | False | _The number of cores assigned to the container. A container can use all available cores by default._ |
| `cpulimit` | number | False | False | _Limit of CPU usage.

NOTE: If the computer has 2 CPUs, it has a total of '2' CPU time. Value '0' indicates no CPU limit._ |
| `cpuunits` | integer | False | False | _CPU weight for a VM. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this VM gets. Number is relative to the weights of all the other running VMs.

NOTE: You can disable fair-scheduler configuration by setting this to 0._ |
| `debug` | boolean | False | False | _Try to be more verbose. For now this only enables debug log-level on start._ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `description` | string | False | False | _Description for the Container. Shown in the web-interface CT's summary. This is saved as comment inside the configuration file._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `features` | string | False | False | _Allow containers access to advanced features._ |
| `hookscript` | string | False | False | _Script that will be exectued during various steps in the containers lifetime._ |
| `hostname` | string | False | False | _Set a host name for the container._ |
| `lock` | string | False | False | _Lock/unlock the VM._ |
| `memory` | integer | False | False | _Amount of RAM for the VM in MB._ |
| `mp[n]` | string | False | False | _Use volume as container mount point. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `nameserver` | string | False | False | _Sets DNS server IP address for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver._ |
| `net[n]` | string | False | False | _Specifies network interfaces for the container._ |
| `node` | string | True | False | _The cluster node name._ |
| `onboot` | boolean | False | False | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | False | _OS type. This is used to setup configuration inside the container, and corresponds to lxc setup scripts in /usr/share/lxc/config/<ostype>.common.conf. Value 'unmanaged' can be used to skip and OS specific setup._ |
| `protection` | boolean | False | False | _Sets the protection flag of the container. This will prevent the CT or CT's disk remove/update operation._ |
| `revert` | string | False | False | _Revert a pending change._ |
| `rootfs` | string | False | False | _Use volume as container root._ |
| `searchdomain` | string | False | False | _Sets DNS search domains for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver._ |
| `startup` | string | False | False | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `swap` | integer | False | False | _Amount of SWAP for the VM in MB._ |
| `tags` | string | False | False | _Tags of the Container. This is only meta information._ |
| `template` | boolean | False | False | _Enable/disable Template._ |
| `timezone` | string | False | False | _Time zone to use in the container. If option isn't set, then nothing will be done. Can be set to 'host' to match the host time zone, or an arbitrary time zone option from /usr/share/zoneinfo/zone.tab_ |
| `tty` | integer | False | False | _Specify the number of tty available to the container_ |
| `unprivileged` | boolean | False | False | _Makes the container run as unprivileged user. (Should not be modified manually.)_ |
| `unused[n]` | string | False | False | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_ceph_mon_createmon
_Create Ceph Monitor and Manager_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `mon_address` | string | False | False | _Overwrites autodetected monitor IP address(es). Must be in the public network(s) of Ceph._ |
| `monid` | string | False | False | _The ID for the monitor, when omitted the same as the nodename_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_capabilities_qemu_machines_types
_Get available QEMU/KVM machine types._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### nodes_ceph_init
_Create initial ceph default configuration and setup symlinks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cluster_network` | string | False | False | _Declare a separate cluster network, OSDs will routeheartbeat, object replication and recovery traffic over it_ |
| `disable_cephx` | boolean | False | False | _Disable cephx authentication.

WARNING: cephx is a security feature protecting against man-in-the-middle attacks. Only consider disabling cephx if your network is private!_ |
| `min_size` | integer | False | False | _Minimum number of available replicas per object to allow I/O_ |
| `network` | string | False | False | _Use specific network for all ceph related traffic_ |
| `node` | string | True | False | _The cluster node name._ |
| `pg_bits` | integer | False | False | _Placement group bits, used to specify the default number of placement groups.

NOTE: 'osd pool default pg num' does not work for default pools._ |
| `size` | integer | False | False | _Targeted number of replicas per object_ |
### nodes_qemu_snapshot_config_get_snapshot_config
_Get snapshot configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | True | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_rrd
_Read VM RRD statistics (returns PNG)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `ds` | string | True | False | _The list of datasources you want to display._ |
| `node` | string | True | False | _The cluster node name._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_groups_delete_group
_Delete group._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `groupid` | string | True | False | _Description unavailable._ |
### cluster_ha_status_current_status
_Get HA manger status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### cluster_ceph_flags_update_flag
_Set or clear (unset) a specific ceph flag_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `flag` | string | True | False | _The ceph flag to update_ |
| `value` | boolean | True | False | _The new value of the flag_ |
### nodes_storage_prunebackups_delete
_Prune backups. Only those using the standard naming scheme are considered._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `prune_backups` | string | False | False | _Use these retention options instead of those from the storage configuration._ |
| `storage` | string | True | False | _The storage identifier._ |
| `type` | string | False | False | _Either 'qemu' or 'lxc'. Only consider backups for guests of this type._ |
| `vmid` | integer | False | False | _Only prune backups for this VM._ |
### nodes_wakeonlan
_Try to wake a node via 'wake on LAN' network packet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _target node for wake on LAN packet_ |
### cluster_options_get_options
_Get datacenter options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_qemu_cloudinit_dump_cloudinit_generated_config_dump
_Get automatically generated cloudinit config._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `type` | string | True | False | _Config type._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_sdn_dns_update
_Update sdn dns object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dns` | string | True | False | _The SDN dns object identifier._ |
| `key` | string | False | True | _Description unavailable._ |
| `reversemaskv6` | integer | False | False | _Description unavailable._ |
| `ttl` | integer | False | False | _Description unavailable._ |
| `url` | string | False | False | _Description unavailable._ |
### nodes_qemu_agent_fsfreeze-freeze
_Execute fsfreeze-freeze._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_ceph_osd_in
_ceph osd in_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `osdid` | integer | True | False | _OSD ID_ |
### cluster_sdn_ipams_update
_Update sdn ipam object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `ipam` | string | True | False | _The SDN ipam object identifier._ |
| `section` | integer | False | False | _Description unavailable._ |
| `token` | string | False | False | _Description unavailable._ |
| `url` | string | False | False | _Description unavailable._ |
### nodes_firewall_rules_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | False | _The cluster node name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
### nodes_lxc_firewall_aliases_read_alias
_Read alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _Alias name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_disks_lvm_index
_List LVM Volume Groups_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_ceph_flags_get_flag
_Get the status of a specific ceph flag._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `flag` | string | True | False | _The name of the flag name to get._ |
### nodes_lxc_rrddata
_Read VM RRD statistics_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `node` | string | True | False | _The cluster node name._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### access_roles_delete_role
_Delete role._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `roleid` | string | True | False | _Description unavailable._ |
### nodes_ceph_mds_destroymds
_Destroy Ceph Metadata Server_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | False | _The name (ID) of the mds_ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_storage_status_read_status
_Read storage status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
### cluster_firewall_groups_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `group` | string | True | False | _Security Group name._ |
| `pos` | integer | False | False | _Update rule at position <pos>._ |
### nodes_apt_repositories_add_repository
_Add a standard repository to the configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Digest to detect modifications._ |
| `handle` | string | True | False | _Handle that identifies a repository._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_subscription_get
_Read subscription info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### access_users_token_generate_token
_Generate a new API token for a specific user. NOTE: returns API token value, which needs to be stored as it cannot be retrieved afterwards!_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | False | _Description unavailable._ |
| `expire` | integer | False | False | _API token expiration date (seconds since epoch). '0' means no expiration date._ |
| `privsep` | boolean | False | False | _Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user._ |
| `tokenid` | string | True | False | _User-specific token identifier._ |
| `userid` | string | True | False | _User ID_ |
### nodes_ceph_fs_createfs
_Create a Ceph filesystem_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | False | _Configure the created CephFS as storage for this cluster._ |
| `name` | string | False | False | _The ceph filesystem name._ |
| `node` | string | True | False | _The cluster node name._ |
| `pg_num` | integer | False | False | _Number of placement groups for the backing data pool. The metadata pool will use a quarter of this._ |
### cluster_sdn_zones_read
_Read sdn zone configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | False | _Display pending config._ |
| `running` | boolean | False | False | _Display running config._ |
| `zone` | string | True | False | _The SDN zone object identifier._ |
### cluster_acme_account_update_account
_Update existing ACME account information with CA. Note: not specifying any new account information triggers a refresh._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `contact` | string | False | False | _Contact email addresses._ |
| `name` | string | False | False | _ACME account config file name._ |
### cluster_acme_plugins_update_plugin
_Update ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api` | string | False | False | _API plugin name_ |
| `data` | string | False | False | _DNS plugin data. (base64 encoded)_ |
| `delete` | string | False | False | _A list of settings you want to delete._ |
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | False | _Flag to disable the config._ |
| `id` | string | True | False | _ACME Plugin ID name_ |
| `nodes` | string | False | False | _List of cluster node names._ |
| `validation_delay` | integer | False | False | _Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records._ |
### nodes_services_stop_service_stop
_Stop service._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | True | False | _Service ID_ |
### nodes_qemu_agent_fsfreeze-thaw
_Execute fsfreeze-thaw._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_status_stop_vm_stop
_Stop the container. This will abruptly stop all processes running in the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `skiplock` | boolean | False | False | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_vncproxy
_Creates a TCP VNC proxy connections._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `height` | integer | False | False | _sets the height of the console in pixels._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
| `websocket` | boolean | False | False | _use websocket instead of standard VNC._ |
| `width` | integer | False | False | _sets the width of the console in pixels._ |
### nodes_certificates_acme_certificate_renew_certificate
_Renew existing certificate from CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _Force renewal even if expiry is more than 30 days away._ |
| `node` | string | True | False | _The cluster node name._ |
### cluster_ceph_status
_Get ceph status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
### nodes_stopall
_Stop all VMs and Containers._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vms` | string | False | False | _Only consider Guests with these IDs._ |
### nodes_services_reload_service_reload
_Reload service. Falls back to restart if service cannot be reloaded._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | True | False | _Service ID_ |
### nodes_status
_Read node status_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### cluster_sdn_dns_read
_Read sdn dns configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns` | string | True | False | _The SDN dns object identifier._ |
### nodes_apt_versions
_Get package information for important Proxmox packages._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
### access_password_change_password
_Change user password._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `password` | string | True | True | _The new password._ |
| `userid` | string | True | False | _User ID_ |
### nodes_lxc_firewall_options_get_options
_Get VM firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_firewall_aliases_remove_alias
_Remove IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | False | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | False | _Alias name._ |
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_certificates_custom_upload_custom_cert
_Upload or update custom certificate chain and key._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `certificates` | string | True | False | _PEM encoded certificate (chain)._ |
| `force` | boolean | False | False | _Overwrite existing custom or ACME certificate files._ |
| `key` | string | False | True | _PEM encoded private key._ |
| `node` | string | True | False | _The cluster node name._ |
| `restart` | boolean | False | False | _Restart pveproxy._ |
### access_tfa_verify_tfa
_Finish a u2f challenge._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response` | string | True | False | _The response to the current authentication challenge._ |
### nodes_services_state_service_state
_Read service properties_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `service` | string | True | False | _Service ID_ |
### nodes_storage_rrd
_Read storage RRD statistics (returns PNG)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | False | _The RRD consolidation function_ |
| `ds` | string | True | False | _The list of datasources you want to display._ |
| `node` | string | True | False | _The cluster node name._ |
| `storage` | string | True | False | _The storage identifier._ |
| `timeframe` | string | True | False | _Specify the time frame you are interested in._ |
### nodes_lxc_feature_vm_feature
_Check if feature for virtual machine is available._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `feature` | string | True | False | _Feature to check._ |
| `node` | string | True | False | _The cluster node name._ |
| `snapname` | string | False | False | _The name of the snapshot._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_lxc_template
_Create a Template._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_replication_log_read_job_log
_Read replication job log._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `id` | string | True | False | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `limit` | integer | False | False | _Description unavailable._ |
| `node` | string | True | False | _The cluster node name._ |
| `start` | integer | False | False | _Description unavailable._ |
### nodes_lxc_firewall_refs
_Lists possible IPSet/Alias reference which are allowed in source/dest properties._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `type` | string | False | False | _Only list references of specified type._ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### nodes_certificates_acme_certificate_new_certificate
_Order a new certificate from ACME-compatible CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | False | _Overwrite existing custom certificate._ |
| `node` | string | True | False | _The cluster node name._ |
### nodes_qemu_termproxy
_Creates a TCP proxy connections._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |
| `serial` | string | False | False | _opens a serial terminal (defaults to display)_ |
| `vmid` | integer | True | False | _The (unique) ID of the VM._ |
### cluster_config_nodes_delnode
_Removes a node from the cluster configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | False | _The cluster node name._ |



## Sensors

There are no sensors available for this pack.



## Authentication


## Limitations


## References

  * [requests](https://docs.python-requests.org/en/latest/)
  * [esprima](https://github.com/Kronuz/esprima-python)
  * [proxmoxer](https://github.com/proxmoxer/proxmoxer)
  * [jinja2](https://palletsprojects.com/p/jinja/)


## Acknowledgements


<sub>Documentation generated using [pack2md](https://github.com/nzlosh/pack2md)</sub>