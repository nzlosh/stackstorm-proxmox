# Proxmox integration pack

> Enable StackStorm to interact with the Proxmox APIv2.
Carlos <nzlosh@yahoo.com>

## Action generation

Actions are generated from the Proxmox API documentation which can be read directly from the
local filesystem or via the Proxmox web interface.  The pack has been generated against Proxmox v6.1 through to v8.0

## Pack versioning

Each Proxmox API version is stored as a git branch that corresponds to the version.  Git tags are used to link the
API version to the pack version.  The branch format is `v<major>.<minor>` and the tag format is `v<major>.<minor>_<pack_major>.<pack_minor>.<pack_patch>`

The reasons for organising the code in such a way is to allow pack installations based on the Proxmox version and/or the pack version.

For an example: if someone operates Proxmox 7.2, they can install the pack from the latest release with the following command

`st2 pack install https://github.com/nzlosh/stackstorm-proxmox=v7.2`

The same person could also use the tag to get a specific version of the `v7.2` branch with the tag.

`st2 pack install https://github.com/nzlosh/stackstorm-proxmox=v7.2_v1.0.2`

### Installation

The recommended method to generate the pack is to create a Python virtual environment, install the
dependencies and run the generator.  The generator code dependencies are defined in
`gen-requirements.txt` which is found in the root directory of the repository.

1. Get the pack
    `git clone <pack repository>`
2. Create a Python virtual environment
    `python -m venv <path to virtualenv>`
3. Activate the Python virtual environment.
    `activate <path to virtualenv>/bin/activate`
4. Install generator dependencies.
    `cd <pack repository>; pip install -r gen-requirements.txt`
5. Run code generator
    `cd <pack repository>/contrib; ./proxmox_pack_generator.py <your options>`
6. Deactivate Python virtual environment.
    `deactivate`

### Usage

The generator is located in the `contrib` directory of the repository.  It parses the `apidoc.js`
file to extract the available API method signatures.  The generator accepts the api_source file in
the form of a local filesystem filename (e.g. `/home/my_account/apidoc.js`) or a URL to Proxmox's
API root (e.g. `https://my_proxmox.example.local:8006`)

```
$ ./proxmox_pack_generator.py -h
usage: proxmox_pack_generator.py [-h] [--username USERNAME]
                                 [--password PASSWORD] [--realm REALM]
                                 --pack_path PACK_PATH
                                 api_source

Proxmox pack action generator.

positional arguments:
  api_source            Source of API documentation. Can be filename or url to
                        apidoc.

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME   Proxmox API username
  --password PASSWORD   Proxmox API password
  --realm REALM         Proxmox API authentication realm
  --pack_path PACK_PATH
                        Path to pack where files will be written.
```

## Configuration

### Profiles
The Proxmox pack uses the notion of profiles to make it simple to target proxmox servers.  Each action
takes a profile_name variable that will use the connection information from the pack configuration for
that action execution.

Below is an example that defines `dev`, `preprod`, `prod` profiles and will default to the `prod` profile
if no profile is supplied to the action execution.
```
default_profile: prod
profiles:
  - host: proxmox.preprod.example.local
    name: preprod
    password: zzz
    port: 8006
    auth_realm: LDAP
    username: proxmox_admin
    verify_tls: true
  - host: proxmox.example.local
    name: prod
    password: zzz
    port: 8006
    auth_realm: LDAP
    username: proxmox_admin
    verify_tls: true
  - host: proxmox.dev.example.local
    name: dev
    password: yyy
    port: 8006
    auth_realm: pam
    username: dev_user
    verify_tls: false
```

The following options are required to be configured for the pack to work correctly.

| Option | Type | Required | Secret | Description |
|---|---|---|---|---|
| `default_profile` | string | True |  | The default profile to use in actions when none is given. |
| `profiles` | array | True |  | A profile describing environment and credentials require to establish a connection. |
## Actions


The pack provides the following actions:

### cluster_firewall_ipset_create_ipset
_Create new IPSet_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `rename` | string | False | default | _Rename an existing IPSet. You can set 'rename' to the same value as 'name' to update the 'comment' of an existing IPSet._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_status_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_startall
_Start all VMs and containers located on this node (by default only those with onboot=1)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _Issue start command even if virtual guest have 'onboot' not set or set to off._ |
| `node` | string | True | default | _The cluster node name._ |
| `vms` | string | False | default | _Only consider guests from this comma separated list of VMIDs._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_log
_Read cluster log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_max` | integer | False | default | _Maximum number of entries._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_plugins_id_get_plugin_config
_Get ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Unique identifier for ACME plugin instance._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_upload
_Upload templates and ISO images._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `content` | string | True | default | _Content type._ |
| `filename` | string | True | default | _The name of the file to create._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `tmpfilename` | string | False | default | _The source file name. This parameter is usually set by the REST handler. You can only overwrite it when connecting to the trusted port on localhost._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_read
_Read sdn vnet configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_exec
_Executes the given command in the vm via the guest-agent and returns an object with the pid._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | False | default | _The command as a list of program + arguments_ |
| `input_data` | string | False | default | _Data to pass as 'input-data' to the guest. Usually treated as STDIN to 'command'._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_rules_pos_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_aliases_get_aliases
_List aliases_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_totem
_Get corosync totem protocol settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hosts_get_etc_hosts
_Get the content of /etc/hosts._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_macros_get_macros
_List available macros_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot_snapname_snapshot_cmd_idx
__

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mgr_index
_MGR directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_rules_get_rules
_List rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot_snapname_config_get_snapshot_config
_Get snapshot configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mds_name_createmds
_Create Ceph Metadata Server (MDS)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `hotstandby` | boolean | False | default | _Determines whether a ceph-mds daemon should poll and replay the log of an active MDS. Faster switch on MDS failure, but needs more idle resources._ |
| `name` | string | False | default | _The ID for the mds, when omitted the same as the nodename_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_osd_osdid_scrub
_Instruct the OSD to scrub._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `deep` | boolean | False | default | _If set, instructs a deep scrub instead of a normal one._ |
| `node` | string | True | default | _The cluster node name._ |
| `osdid` | integer | True | default | _OSD ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_roles_roleid_update_role
_Update an existing role._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `append` | boolean | False | default | _Description unavailable._ |
| `privs` | string | False | default | _Description unavailable._ |
| `roleid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_template
_Create a Template._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | False | default | _If you want to convert only 1 disk to base image._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_rules
_List ceph rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_zones_create
_Create a new sdn zone object._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bridge` | string | False | default | _Description unavailable._ |
| `controller` | string | False | default | _Frr router name_ |
| `dns` | string | False | default | _dns api server_ |
| `dnszone` | string | False | default | _dns domain zone  ex: mydomain.com_ |
| `dp_id` | integer | False | default | _Faucet dataplane id_ |
| `exitnodes` | string | False | default | _List of cluster node names._ |
| `ipam` | string | False | default | _use a specific ipam_ |
| `mac` | string | False | default | _Anycast logical router mac address_ |
| `mtu` | integer | False | default | _MTU_ |
| `nodes` | string | False | default | _List of cluster node names._ |
| `peers` | string | False | default | _peers address list._ |
| `reversedns` | string | False | default | _reverse dns api server_ |
| `tag` | integer | False | default | _Service-VLAN Tag_ |
| `prox_type` | string | True | default | _Plugin type._ |
| `vlan_protocol` | string | False | default | _Description unavailable._ |
| `vrf_vxlan` | integer | False | default | _l3vni._ |
| `zone` | string | True | default | _The SDN zone object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_aliases_get_aliases
_List aliases_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_domains_realm_delete
_Delete an authentication server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `realm` | string | True | default | _Authentication domain ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_replication_id_read
_Read replication job configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_exec_status
_Gets the status of the given pid started by the guest-agent_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pid` | integer | True | default | _The PID to query_ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_rules_pos_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_timezone
_Execute get-timezone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hardware_index
_Index of hardware types_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mgr_id_destroymgr
_Destroy Ceph Manager._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _The ID of the manager_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_start
_Start ceph services._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | False | default | _Ceph service name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_flags_flag_unset_flag
_Unset a ceph flag_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `flag` | string | True | default | _The ceph flag to unset_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_iface_network_config
_Read network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `iface` | string | True | default | _Network interface name._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_subnets_subnet_update
_Update sdn subnet object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dnszoneprefix` | string | False | default | _dns domain zone prefix  ex: 'adm' -> <hostname>.adm.mydomain.com_ |
| `gateway` | string | False | default | _Subnet Gateway: Will be assign on vnet for layer3 zones_ |
| `snat` | boolean | False | default | _enable masquerade for this subnet if pve-firewall_ |
| `subnet` | string | True | default | _The SDN subnet object identifier._ |
| `vnet` | string | False | default | _associated vnet_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_tasks_upid_status_read_task_status
_Read task status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `upid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_tasks_upid_upid_index
__

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `upid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_controllers_controller_update
_Update sdn controller object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `asn` | integer | False | default | _autonomous system number_ |
| `controller` | string | True | default | _The SDN controller object identifier._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `ebgp` | boolean | False | default | _Enable ebgp. (remote-as external)_ |
| `ebgp_multihop` | integer | False | default | _Description unavailable._ |
| `loopback` | string | False | default | _source loopback interface._ |
| `node` | string | False | default | _The cluster node name._ |
| `peers` | string | False | default | _peers address list._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_ipams_index
_SDN ipams index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Only list sdn ipams of specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_name_cidr_remove_ip
_Remove IP or Network from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_name_get_ipset
_List IPSet content_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _IP set name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_termproxy
_Creates a TCP proxy connections._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `serial` | string | False | default | _opens a serial terminal (defaults to display)_ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_acl_update_acl
_Update Access Control List (add or remove permissions)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | boolean | False | default | _Remove permissions (instead of adding it)._ |
| `groups` | string | False | default | _List of groups._ |
| `path` | string | True | default | _Access control path_ |
| `propagate` | boolean | False | default | _Allow to propagate (inherit) permissions._ |
| `roles` | string | True | default | _List of roles._ |
| `tokens` | string | False | default | _List of API tokens._ |
| `users` | string | False | default | _List of users._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_refs
_Lists possible IPSet/Alias reference which are allowed in source/dest properties._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prox_type` | string | False | default | _Only list references of specified type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_tfa_read_user_tfa_type
_Get user TFA types (Personal and Realm)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_reboot_vm_reboot
_Reboot the container by shutting it down, and starting it again. Applies pending changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `timeout` | integer | False | default | _Wait maximal timeout seconds for the shutdown._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_subscription_update
_Update subscription info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _Always connect to server, even if we have up to date info inside local cache._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_status_node_cmd
_Reboot or shutdown a node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | True | default | _Specify the command._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_service_reload
_Reload service. Falls back to restart if service cannot be reloaded._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | True | default | _Service ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_crush
_Get OSD crush map_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_nfs_nfsscan
_Scan remote NFS server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `server` | string | True | default | _The server address (name or IP)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_start_vm_start
_Start the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `debug` | boolean | False | default | _If set, enables very verbose debug log-level on start._ |
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_vmdiridx
_Directory index_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_name_get_ipset
_List IPSet content_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_join_join_info
_Get information needed to join this cluster over the connected node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | False | default | _The node for which the joinee gets the nodeinfo. _ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_metadata
_Get ceph metadata._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `scope` | string | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_spiceshell
_Creates a SPICE shell._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cmd` | string | False | default | _Run specific command or default to login._ |
| `cmd_opts` | string | False | default | _Add parameters to a command. Encoded as null terminated strings._ |
| `node` | string | True | default | _The cluster node name._ |
| `proxy` | string | False | default | _SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI)._ |
| `upgrade` | boolean | False | default | _Deprecated, use the 'cmd' property instead! Run 'apt-get dist-upgrade' instead of normal shell._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_dns_create
_Create a new sdn dns object._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns` | string | True | default | _The SDN dns object identifier._ |
| `key` | string | True | True | _Description unavailable._ |
| `reversemaskv6` | integer | False | default | _Description unavailable._ |
| `reversev6mask` | integer | False | default | _Description unavailable._ |
| `ttl` | integer | False | default | _Description unavailable._ |
| `prox_type` | string | True | default | _Plugin type._ |
| `url` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_aliases_name_update_alias
_Update IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `rename` | string | False | default | _Rename an existing alias._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_rules_pos_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_apiversion_join_api_version
_Return the version of the cluster join API available on this node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_sid_relocate
_Request resource relocatzion to another node. This stops the service on the old node, and restarts it on the target node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _Target node._ |
| `sid` | string | True | default | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_vzdump_defaults
_Get the currently configured vzdump defaults._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | False | default | _The storage identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_apt_update_list_updates
_List available updates._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_name_get_ipset
_List IPSet content_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_apt_versions
_Get package information for important Proxmox packages._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_list
_List local disks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `include_partitions` | boolean | False | default | _Also include partitions._ |
| `node` | string | True | default | _The cluster node name._ |
| `skipsmart` | boolean | False | default | _Skip smart checks._ |
| `prox_type` | string | False | default | _Only list specific types of disks._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_replication_id_delete
_Mark replication job for removal._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _Will remove the jobconfig entry, but will not cleanup._ |
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `keep` | boolean | False | default | _Keep replicated data at target (do not remove)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_groups_groupid_update_group
_Update group data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `groupid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_refs
_Lists possible IPSet/Alias reference which are allowed in source/dest properties._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Only list references of specified type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_subscription_set
_Set subscription key._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | True | _Proxmox VE subscription key_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_file_write
_Writes the given file via guest agent._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `content` | string | True | default | _The content to write into the file._ |
| `file` | string | True | default | _The path to the file._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_index
_SDN vnets index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_rrd
_Read storage RRD statistics (returns PNG)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `ds` | string | True | default | _The list of datasources you want to display._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_flags_set_flags
_Set/Unset multiple ceph flags at once._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `nobackfill` | boolean | False | default | _Backfilling of PGs is suspended._ |
| `nodeep_scrub` | boolean | False | default | _Deep Scrubbing is disabled._ |
| `nodown` | boolean | False | default | _OSD failure reports are being ignored, such that the monitors will not mark OSDs down._ |
| `noin` | boolean | False | default | _OSDs that were previously marked out will not be marked back in when they start._ |
| `noout` | boolean | False | default | _OSDs will not automatically be marked out after the configured interval._ |
| `norebalance` | boolean | False | default | _Rebalancing of PGs is suspended._ |
| `norecover` | boolean | False | default | _Recovery of PGs is suspended._ |
| `noscrub` | boolean | False | default | _Scrubbing is disabled._ |
| `notieragent` | boolean | False | default | _Cache tiering activity is suspended._ |
| `noup` | boolean | False | default | _OSDs are not allowed to start._ |
| `pause` | boolean | False | default | _Pauses read and writes._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_aliases_name_remove_alias
_Remove IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _Alias name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_controllers_index
_SDN controllers index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `prox_type` | string | False | default | _Only list sdn controllers of specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_groups_index
_Group index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_fsfreeze_freeze
_Execute fsfreeze-freeze._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_osd_osdid_in
_ceph osd in_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `osdid` | integer | True | default | _OSD ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_replication_id_status_job_status
_Get replication job status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot_snapshot_list
_List all snapshots._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_flags_flag_update_flag
_Set or clear (unset) a specific ceph flag_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `flag` | string | True | default | _The ceph flag to update_ |
| `value` | boolean | True | default | _The new value of the flag_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_version
_API version details_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_subnets_subnet_read
_Read sdn subnet configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `subnet` | string | True | default | _The SDN subnet object identifier._ |
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_create_ipset
_Create new IPSet_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `rename` | string | False | default | _Rename an existing IPSet. You can set 'rename' to the same value as 'name' to update the 'comment' of an existing IPSet._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_account_name_deactivate_account
_Deactivate existing ACME account at CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | False | default | _ACME account config file name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot
_Snapshot a VM._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `description` | string | False | default | _A textual description or comment._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `vmstate` | boolean | False | default | _Save the vmstate_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_pools_name_destroypool
_Destroy pool_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _If true, destroys pool even if in use_ |
| `name` | string | True | default | _The name of the pool. It must be unique._ |
| `node` | string | True | default | _The cluster node name._ |
| `remove_storages` | boolean | False | default | _Remove all pveceph-managed storages configured for this pool_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mon_monid_createmon
_Create Ceph Monitor and Manager_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `mon_address` | string | False | default | _Overwrites autodetected monitor IP address. Must be in the public network of ceph._ |
| `monid` | string | False | default | _The ID for the monitor, when omitted the same as the nodename_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_group_create_rule
_Create new rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `group` | string | True | default | _Security Group name._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | True | default | _Rule type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent
_Execute Qemu Guest Agent commands._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | True | default | _The QGA command._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_custom_upload_custom_cert
_Upload or update custom certificate chain and key._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `certificates` | string | True | default | _PEM encoded certificate (chain)._ |
| `force` | boolean | False | default | _Overwrite existing custom or ACME certificate files._ |
| `key` | string | False | True | _PEM encoded private key._ |
| `node` | string | True | default | _The cluster node name._ |
| `restart` | boolean | False | default | _Restart pveproxy._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_plugins_id_update_plugin
_Update ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api` | string | False | default | _API plugin name_ |
| `data` | string | False | default | _DNS plugin data. (base64 encoded)_ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | default | _Flag to disable the config._ |
| `prox_id` | string | True | default | _ACME Plugin ID name_ |
| `nodes` | string | False | default | _List of cluster node names._ |
| `validation_delay` | integer | False | default | _Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_osd_createosd
_Create OSD_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `crush_device_class` | string | False | default | _Set the device class of the OSD in crush._ |
| `db_dev` | string | False | default | _Block device name for block.db._ |
| `db_size` | number | False | default | _Size in GiB for block.db._ |
| `dev` | string | True | default | _Block device name._ |
| `encrypted` | boolean | False | default | _Enables encryption of the OSD._ |
| `node` | string | True | default | _The cluster node name._ |
| `wal_dev` | string | False | default | _Block device name for block.wal._ |
| `wal_size` | number | False | default | _Size in GiB for block.wal._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_resume_vm_resume
_Resume virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `nocheck` | boolean | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_index
_Cluster node index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_create
_Create a new sdn vnet object._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `alias` | string | False | default | _alias name of the vnet_ |
| `tag` | integer | False | default | _vlan or vxlan id_ |
| `prox_type` | string | False | default | _Type_ |
| `vlanaware` | boolean | False | default | _Allow vm VLANs to pass through this vnet._ |
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `zone` | string | True | default | _zone id_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_cephindex
_Cluster ceph index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_status_read_status
_Read storage status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_config_vm_config
_Get container configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `current` | boolean | False | default | _Get current values (instead of pending values)._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapshot` | string | False | default | _Fetch config values from given snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_rules_pos_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_fsfreeze_status
_Execute fsfreeze-status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_nextid
_Get next free VMID. If you pass an VMID it will raise an error if the ID is already used._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `vmid` | integer | False | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_plugins_id_delete_plugin
_Delete ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Unique identifier for ACME plugin instance._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_roles_create_role
_Create new role._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `privs` | string | False | default | _Description unavailable._ |
| `roleid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_vncwebsocket
_Opens a weksocket for VNC traffic._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `port` | integer | True | default | _Port number returned by previous vncproxy call._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `vncticket` | string | True | default | _Ticket from previous call to vncproxy._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_rrd
_Read VM RRD statistics (returns PNG)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `ds` | string | True | default | _The list of datasources you want to display._ |
| `node` | string | True | default | _The cluster node name._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_spiceproxy
_Returns a SPICE configuration to connect to the CT._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `proxy` | string | False | default | _SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI)._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `ebtables` | boolean | False | default | _Enable ebtables rules cluster wide._ |
| `enable` | integer | False | default | _Enable or disable the firewall cluster wide._ |
| `log_ratelimit` | string | False | default | _Log ratelimiting settings_ |
| `policy_in` | string | False | default | _Input policy._ |
| `policy_out` | string | False | default | _Output policy._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### pools_poolid_delete_pool
_Delete pool._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `poolid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_termproxy
_Creates a VNC Shell proxy._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cmd` | string | False | default | _Run specific command or default to login._ |
| `cmd_opts` | string | False | default | _Add parameters to a command. Encoded as null terminated strings._ |
| `node` | string | True | default | _The cluster node name._ |
| `upgrade` | boolean | False | default | _Deprecated, use the 'cmd' property instead! Run 'apt-get dist-upgrade' instead of normal shell._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_aliases_name_read_alias
_Read alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_vmcmdidx
_Directory index_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_metrics_server_id_read
_Read metric server configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_diridx
__

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_options_get_options
_Get Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_roles_roleid_read_role
_Get role configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `roleid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_disks
_List local disks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prox_type` | string | False | default | _Only list specific types of disks._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_metrics_server_id_update
_Update metric server configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_path_prefix` | string | False | default | _An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy._ |
| `bucket` | string | False | default | _The InfluxDB bucket/db. Only necessary when using the http v2 api._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | default | _Flag to disable the plugin._ |
| `prox_id` | string | True | default | _The ID of the entry._ |
| `influxdbproto` | string | False | default | _Description unavailable._ |
| `max_body_size` | integer | False | default | _InfluxDB max-body-size in bytes. Requests are batched up to this size._ |
| `mtu` | integer | False | default | _MTU for metrics transmission over UDP_ |
| `organization` | string | False | default | _The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api._ |
| `path` | string | False | default | _root graphite path (ex: proxmox.mycluster.mykey)_ |
| `port` | integer | True | default | _server network port_ |
| `proto` | string | False | default | _Protocol to send graphite data. TCP or UDP (default)_ |
| `server` | string | True | default | _server dns name or IP address_ |
| `timeout` | integer | False | default | _graphite TCP socket timeout (default=1)_ |
| `token` | string | False | default | _The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_content_volume_updateattributes
_Update volume attributes_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `notes` | string | False | default | _The new notes._ |
| `storage` | string | False | default | _The storage identifier._ |
| `volume` | string | True | default | _Volume identifier_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_capabilities_qemu_qemu_caps_index
_QEMU capabilities index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_flags_flag_set_flag
_Set a specific ceph flag_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `flag` | string | True | default | _The ceph flag to set_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_delete_user
_Delete user._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_name_cidr_remove_ip
_Remove IP or Network from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_aliases_create_alias
_Create IP or Network Alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `name` | string | True | default | _Alias name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_service_stop
_Stop service._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | True | default | _Service ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backupinfo_get_backupinfo
_Stub, waits for future use._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_config_vm_config
_Get the virtual machine configuration with pending configuration changes applied. Set the 'current' parameter to get the current configuration instead._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `current` | boolean | False | default | _Get current values (instead of pending values)._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapshot` | string | False | default | _Fetch config values from given snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_index
_Service list._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_index
_User index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `enabled` | boolean | False | default | _Optional filter for enable property._ |
| `full` | boolean | False | default | _Include group and token information._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_log
_Read firewall log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `start` | integer | False | default | _Description unavailable._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_create_security_group
_Create new security group._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `group` | string | True | default | _Security Group name._ |
| `rename` | string | False | default | _Rename/update an existing security group. You can set 'rename' to the same value as 'name' to update the 'comment' of an existing group._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_tasks_upid_log_read_task_log
_Read task log._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `start` | integer | False | default | _Description unavailable._ |
| `upid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_zones_index
_SDN zones index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `prox_type` | string | False | default | _Only list SDN zones of specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_challenge_schema_challengeschema
_Get schema of ACME challenge types._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_iface_update_network
_Update network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `address` | string | False | default | _IP address._ |
| `address6` | string | False | default | _IP address._ |
| `autostart` | boolean | False | default | _Automatically start interface on boot._ |
| `bond_primary` | string | False | default | _Specify the primary interface for active-backup bond._ |
| `bond_mode` | string | False | default | _Bonding mode._ |
| `bond_xmit_hash_policy` | string | False | default | _Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes._ |
| `bridge_ports` | string | False | default | _Specify the interfaces you want to add to your bridge._ |
| `bridge_vlan_aware` | boolean | False | default | _Enable bridge vlan support._ |
| `cidr` | string | False | default | _IPv4 CIDR._ |
| `cidr6` | string | False | default | _IPv6 CIDR._ |
| `comments` | string | False | default | _Comments_ |
| `comments6` | string | False | default | _Comments_ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `gateway` | string | False | default | _Default gateway address._ |
| `gateway6` | string | False | default | _Default ipv6 gateway address._ |
| `iface` | string | True | default | _Network interface name._ |
| `mtu` | integer | False | default | _MTU._ |
| `netmask` | string | False | default | _Network mask._ |
| `netmask6` | integer | False | default | _Network mask._ |
| `node` | string | True | default | _The cluster node name._ |
| `ovs_bonds` | string | False | default | _Specify the interfaces used by the bonding device._ |
| `ovs_bridge` | string | False | default | _The OVS bridge associated with a OVS port. This is required when you create an OVS port._ |
| `ovs_options` | string | False | default | _OVS interface options._ |
| `ovs_ports` | string | False | default | _Specify the interfaces you want to add to your bridge._ |
| `ovs_tag` | integer | False | default | _Specify a VLan tag (used by OVSPort, OVSIntPort, OVSBond)_ |
| `slaves` | string | False | default | _Specify the interfaces used by the bonding device._ |
| `prox_type` | string | True | default | _Network interface type_ |
| `vlan_id` | integer | False | default | _vlan-id for a custom named vlan interface (ifupdown2 only)._ |
| `vlan_raw_device` | string | False | default | _Specify the raw interface for the vlan interface._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_aliases_get_aliases
_List aliases_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_account_name_update_account
_Update existing ACME account information with CA. Note: not specifying any new account information triggers a refresh._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `contact` | string | False | default | _Contact email addresses._ |
| `name` | string | False | default | _ACME account config file name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_create
_Generate new cluster configuration. If no links given, default to local IP address as link0._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `clustername` | string | True | default | _The name of the cluster._ |
| `link_list` | string | False | default | _Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)_ |
| `nodeid` | integer | False | default | _Node id for this node._ |
| `votes` | integer | False | default | _Number of votes for this node._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_feature_vm_feature
_Check if feature for virtual machine is available._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `feature` | string | True | default | _Feature to check._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | False | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_log
_Read firewall log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `start` | integer | False | default | _Description unavailable._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_config_update_vm
_Set container options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `arch` | string | False | default | _OS architecture type._ |
| `cmode` | string | False | default | _Console mode. By default, the console command tries to open a connection to one of the available tty devices. By setting cmode to 'console' it tries to attach to /dev/console instead. If you set cmode to 'shell', it simply invokes a shell inside the container (no login)._ |
| `console` | boolean | False | default | _Attach a console device (/dev/console) to the container._ |
| `cores` | integer | False | default | _The number of cores assigned to the container. A container can use all available cores by default._ |
| `cpulimit` | number | False | default | _Limit of CPU usage.  NOTE: If the computer has 2 CPUs, it has a total of '2' CPU time. Value '0' indicates no CPU limit._ |
| `cpuunits` | integer | False | default | _CPU weight for a VM. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this VM gets. Number is relative to the weights of all the other running VMs.  NOTE: You can disable fair-scheduler configuration by setting this to 0._ |
| `debug` | boolean | False | default | _Try to be more verbose. For now this only enables debug log-level on start._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `description` | string | False | default | _Container description. Only used on the configuration web interface._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `features` | string | False | default | _Allow containers access to advanced features._ |
| `hookscript` | string | False | default | _Script that will be exectued during various steps in the containers lifetime._ |
| `hostname` | string | False | default | _Set a host name for the container._ |
| `lock` | string | False | default | _Lock/unlock the VM._ |
| `memory` | integer | False | default | _Amount of RAM for the VM in MB._ |
| `mp_list` | string | False | default | _Use volume as container mount point. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `nameserver` | string | False | default | _Sets DNS server IP address for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver._ |
| `net_list` | string | False | default | _Specifies network interfaces for the container._ |
| `node` | string | True | default | _The cluster node name._ |
| `onboot` | boolean | False | default | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | default | _OS type. This is used to setup configuration inside the container, and corresponds to lxc setup scripts in /usr/share/lxc/config/<ostype>.common.conf. Value 'unmanaged' can be used to skip and OS specific setup._ |
| `protection` | boolean | False | default | _Sets the protection flag of the container. This will prevent the CT or CT's disk remove/update operation._ |
| `revert` | string | False | default | _Revert a pending change._ |
| `rootfs` | string | False | default | _Use volume as container root._ |
| `searchdomain` | string | False | default | _Sets DNS search domains for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver._ |
| `startup` | string | False | default | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `swap` | integer | False | default | _Amount of SWAP for the VM in MB._ |
| `tags` | string | False | default | _Tags of the Container. This is only meta information._ |
| `template` | boolean | False | default | _Enable/disable Template._ |
| `timezone` | string | False | default | _Time zone to use in the container. If option isn't set, then nothing will be done. Can be set to 'host' to match the host time zone, or an arbitrary time zone option from /usr/share/zoneinfo/zone.tab_ |
| `tty` | integer | False | default | _Specify the number of tty available to the container_ |
| `unprivileged` | boolean | False | default | _Makes the container run as unprivileged user. (Should not be modified manually.)_ |
| `unused_list` | string | False | default | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_name_delete_ipset
_Delete IPSet_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_current_vm_status
_Get virtual machine status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmlist
_LXC container index (per node)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_metrics_server_id_delete
_Remove Metric server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_prunebackups_dryrun
_Get prune information for backups. NOTE: this is only a preview and might not be what a subsequent prune call does if backups are removed/added in the meantime._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prune_backups` | string | False | default | _Use these retention options instead of those from the storage configuration._ |
| `storage` | string | True | default | _The storage identifier._ |
| `prox_type` | string | False | default | _Either 'qemu' or 'lxc'. Only consider backups for guests of this type._ |
| `vmid` | integer | False | default | _Only consider backups for this guest._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_metrics_server_server_index
_List configured metric servers._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_suspend_vm_suspend
_Suspend the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_rules_pos_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_flags_get_all_flags
_get the status of all ceph flags_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_sdn_zones_zone_content_index
_List zone content._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `zone` | string | True | default | _The SDN zone object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_tfa_change_tfa
_Change user u2f authentication._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | default | _The action to perform_ |
| `config` | string | False | default | _A TFA configuration. This must currently be of type TOTP of not set at all._ |
| `key` | string | False | True | _When adding TOTP, the shared secret value._ |
| `password` | string | False | True | _The current password._ |
| `response` | string | False | default | _Either the the response to the current u2f registration challenge, or, when adding TOTP, the currently valid TOTP value._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### version
_API version details. The result also includes the global datacenter confguration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_directory_create
_Create a Filesystem on an unused disk. Will be mounted under '/mnt/pve/NAME'._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | default | _Configure storage using the directory._ |
| `device` | string | True | default | _The block device you want to create the filesystem on._ |
| `filesystem` | string | False | default | _The desired filesystem._ |
| `name` | string | True | default | _The storage identifier._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_cifs_cifsscan
_Scan remote CIFS server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `domain` | string | False | default | _SMB domain (Workgroup)._ |
| `node` | string | True | default | _The cluster node name._ |
| `password` | string | False | True | _User password._ |
| `server` | string | True | default | _The server address (name or IP)._ |
| `username` | string | False | default | _User name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_acme_certificate_revoke_certificate
_Revoke existing certificate from CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_name_cidr_read_ip
_Read IP or Network settings from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `name` | string | True | default | _IP set name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_plugins_index
_ACME plugin index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Only list ACME plugins of a specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_apt_changelog
_Get package changelogs._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Package name._ |
| `node` | string | True | default | _The cluster node name._ |
| `version` | string | False | default | _Package version._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_subnets_subnet_delete
_Delete sdn subnet object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `subnet` | string | True | default | _The SDN subnet object identifier._ |
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_memory_block_info
_Execute get-memory-block-info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_flags_flag_get_flag
_Get the status of a specific ceph flag._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `flag` | string | True | default | _The name of the flag name to get._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_dns_index
_SDN dns index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Only list sdn dns of specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_roles_index
_Role index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_domains_realm_read
_Get auth server configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `realm` | string | True | default | _Authentication domain ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_name_cidr_remove_ip
_Remove IP or Network from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_create_vm
_Create or restore a container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `arch` | string | False | default | _OS architecture type._ |
| `bwlimit` | number | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `cmode` | string | False | default | _Console mode. By default, the console command tries to open a connection to one of the available tty devices. By setting cmode to 'console' it tries to attach to /dev/console instead. If you set cmode to 'shell', it simply invokes a shell inside the container (no login)._ |
| `console` | boolean | False | default | _Attach a console device (/dev/console) to the container._ |
| `cores` | integer | False | default | _The number of cores assigned to the container. A container can use all available cores by default._ |
| `cpulimit` | number | False | default | _Limit of CPU usage.  NOTE: If the computer has 2 CPUs, it has a total of '2' CPU time. Value '0' indicates no CPU limit._ |
| `cpuunits` | integer | False | default | _CPU weight for a VM. Argument is used in the kernel fair scheduler. The larger the number is, the more CPU time this VM gets. Number is relative to the weights of all the other running VMs.  NOTE: You can disable fair-scheduler configuration by setting this to 0._ |
| `debug` | boolean | False | default | _Try to be more verbose. For now this only enables debug log-level on start._ |
| `description` | string | False | default | _Container description. Only used on the configuration web interface._ |
| `features` | string | False | default | _Allow containers access to advanced features._ |
| `force` | boolean | False | default | _Allow to overwrite existing container._ |
| `hookscript` | string | False | default | _Script that will be exectued during various steps in the containers lifetime._ |
| `hostname` | string | False | default | _Set a host name for the container._ |
| `ignore_unpack_errors` | boolean | False | default | _Ignore errors when extracting the template._ |
| `lock` | string | False | default | _Lock/unlock the VM._ |
| `memory` | integer | False | default | _Amount of RAM for the VM in MB._ |
| `mp_list` | string | False | default | _Use volume as container mount point. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `nameserver` | string | False | default | _Sets DNS server IP address for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver._ |
| `net_list` | string | False | default | _Specifies network interfaces for the container._ |
| `node` | string | True | default | _The cluster node name._ |
| `onboot` | boolean | False | default | _Specifies whether a VM will be started during system bootup._ |
| `ostemplate` | string | True | default | _The OS template or backup file._ |
| `ostype` | string | False | default | _OS type. This is used to setup configuration inside the container, and corresponds to lxc setup scripts in /usr/share/lxc/config/<ostype>.common.conf. Value 'unmanaged' can be used to skip and OS specific setup._ |
| `password` | string | False | True | _Sets root password inside container._ |
| `pool` | string | False | default | _Add the VM to the specified pool._ |
| `protection` | boolean | False | default | _Sets the protection flag of the container. This will prevent the CT or CT's disk remove/update operation._ |
| `restore` | boolean | False | default | _Mark this as restore task._ |
| `rootfs` | string | False | default | _Use volume as container root._ |
| `searchdomain` | string | False | default | _Sets DNS search domains for a container. Create will automatically use the setting from the host if you neither set searchdomain nor nameserver._ |
| `ssh_public_keys` | string | False | default | _Setup public SSH keys (one key per line, OpenSSH format)._ |
| `start` | boolean | False | default | _Start the CT after its creation finished successfully._ |
| `startup` | string | False | default | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `storage` | string | False | default | _Default Storage._ |
| `swap` | integer | False | default | _Amount of SWAP for the VM in MB._ |
| `tags` | string | False | default | _Tags of the Container. This is only meta information._ |
| `template` | boolean | False | default | _Enable/disable Template._ |
| `timezone` | string | False | default | _Time zone to use in the container. If option isn't set, then nothing will be done. Can be set to 'host' to match the host time zone, or an arbitrary time zone option from /usr/share/zoneinfo/zone.tab_ |
| `tty` | integer | False | default | _Specify the number of tty available to the container_ |
| `unique` | boolean | False | default | _Assign a unique random ethernet address._ |
| `unprivileged` | boolean | False | default | _Makes the container run as unprivileged user. (Should not be modified manually.)_ |
| `unused_list` | string | False | default | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_resume_vm_resume
_Resume the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_name_cidr_read_ip
_Read IP or Network settings from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot_snapname_config_update_snapshot_config
_Update snapshot metadata._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `description` | string | False | default | _A textual description or comment._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_index
_List available networks_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prox_type` | string | False | default | _Only list specific interface types._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_service_srvcmdidx
_Directory index_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | True | default | _Service ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_replication_status
_List status of all replication jobs on this node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `guest` | integer | False | default | _Only list replication jobs for this guest._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_acme_certificate_new_certificate
_Order a new certificate from ACME-compatible CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _Overwrite existing custom certificate._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_controllers_controller_read
_Read sdn controller configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `controller` | string | True | default | _The SDN controller object identifier._ |
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_shutdown_vm_shutdown
_Shutdown the container. This will trigger a clean shutdown of the container, see lxc-stop(1) for details._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `forceStop` | boolean | False | default | _Make sure the Container stops._ |
| `node` | string | True | default | _The cluster node name._ |
| `timeout` | integer | False | default | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_replication_create
_Create a new replication job_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description._ |
| `disable` | boolean | False | default | _Flag to disable/deactivate the entry._ |
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `rate` | number | False | default | _Rate limit in mbps (megabytes per second) as floating point number._ |
| `remove_job` | string | False | default | _Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file._ |
| `schedule` | string | False | default | _Storage replication schedule. The format is a subset of `systemd` calendar events._ |
| `source` | string | False | default | _For internal use, to detect if the guest was stolen._ |
| `target` | string | True | default | _Target node._ |
| `prox_type` | string | True | default | _Section type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_token_tokenid_remove_token
_Remove API token for a specific user._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `tokenid` | string | True | default | _User-specific token identifier._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_migrate_migrate_vm
_Migrate the container to another node. Creates a new migration task._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | number | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `force` | boolean | False | default | _Force migration despite local bind / device mounts. NOTE: deprecated, use 'shared' property of mount point instead._ |
| `node` | string | True | default | _The cluster node name._ |
| `online` | boolean | False | default | _Use online/live migration._ |
| `restart` | boolean | False | default | _Use restart migration_ |
| `target` | string | True | default | _Target node._ |
| `timeout` | integer | False | default | _Timeout in seconds for shutdown for restart migration_ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_aplinfo
_Get list of appliances._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_aplinfo_apl_download
_Download appliance templates._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage where the template will be stored_ |
| `template` | string | True | default | _The template which will downloaded_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot_snapname_delsnapshot
_Delete a VM snapshot._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _For removal from config file, even if removing disk snapshots fails._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_group_delete_security_group
_Delete security group._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | default | _Security Group name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_group_pos_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `group` | string | True | default | _Security Group name._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `moveto` | integer | False | default | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | False | default | _Rule type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_token_tokenid_generate_token
_Generate a new API token for a specific user. NOTE: returns API token value, which needs to be stored as it cannot be retrieved afterwards!_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `expire` | integer | False | default | _API token expiration date (seconds since epoch). '0' means no expiration date._ |
| `privsep` | boolean | False | default | _Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user._ |
| `tokenid` | string | True | default | _User-specific token identifier._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_groups_group_read
_Read ha group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | default | _The HA group identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_index
_Node index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_pools_name_getpool
_List pool settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _The name of the pool. It must be unique._ |
| `node` | string | True | default | _The cluster node name._ |
| `verbose` | boolean | False | default | _If enabled, will display additional data(eg. statistics)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### storage_index
_Storage index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Only list storage of specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_rules_pos_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_aliases_name_remove_alias
_Remove IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_vncwebsocket
_Opens a weksocket for VNC traffic._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `port` | integer | True | default | _Port number returned by previous vncproxy call._ |
| `vncticket` | string | True | default | _Ticket from previous call to vncproxy._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_name_delete_ipset
_Delete IPSet_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_cpu_index
_List all custom and default CPU models._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_service_restart
_Hard restart service. Use reload if you want to reduce interruptions._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | True | default | _Service ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_rrddata
_Read VM RRD statistics_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `node` | string | True | default | _The cluster node name._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_migrateall
_Migrate all VMs and Containers._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `maxworkers` | integer | False | default | _Maximal number of parallel migration job. If not set use 'max_workers' from datacenter.cfg, one of both must be set!_ |
| `node` | string | True | default | _The cluster node name._ |
| `target` | string | True | default | _Target node._ |
| `vms` | string | False | default | _Only consider Guests with these IDs._ |
| `with_local_disks` | boolean | False | default | _Enable live storage migration for local disk_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mon_listmon
_Get Ceph monitor list._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_account_account_index
_ACMEAccount index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_dns_dns_update
_Update sdn dns object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dns` | string | True | default | _The SDN dns object identifier._ |
| `key` | string | False | True | _Description unavailable._ |
| `reversemaskv6` | integer | False | default | _Description unavailable._ |
| `ttl` | integer | False | default | _Description unavailable._ |
| `url` | string | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_reboot_vm_reboot
_Reboot the VM by shutting it down, and starting it again. Applies pending changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `timeout` | integer | False | default | _Wait maximal timeout seconds for the shutdown._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_content_volume_delete
_Delete volume_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delay` | integer | False | default | _Time to wait for the task to finish. We return 'null' if the task finish within that time._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | False | default | _The storage identifier._ |
| `volume` | string | True | default | _Volume identifier_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### storage_storage_update
_Update storage configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `blocksize` | string | False | default | _block size_ |
| `bwlimit` | string | False | default | _Set bandwidth/io limits various operations._ |
| `comstar_hg` | string | False | default | _host group for comstar views_ |
| `comstar_tg` | string | False | default | _target group for comstar views_ |
| `content` | string | False | default | _Allowed content types.  NOTE: the value 'rootdir' is used for Containers, and value 'images' for VMs. _ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | default | _Flag to disable the storage._ |
| `domain` | string | False | default | _CIFS domain._ |
| `encryption_key` | string | False | default | _Encryption key. Use 'autogen' to generate one automatically without passphrase._ |
| `fingerprint` | string | False | default | _Certificate SHA 256 fingerprint._ |
| `prox_format` | string | False | default | _Default image format._ |
| `fuse` | boolean | False | default | _Mount CephFS through FUSE._ |
| `is_mountpoint` | string | False | default | _Assume the given path is an externally managed mountpoint and consider the storage offline if it is not mounted. Using a boolean (yes/no) value serves as a shortcut to using the target path in this field._ |
| `krbd` | boolean | False | default | _Always access rbd through krbd kernel module._ |
| `lio_tpg` | string | False | default | _target portal group for Linux LIO targets_ |
| `master_pubkey` | string | False | default | _Base64-encoded, PEM-formatted public RSA key. Used tp encrypt a copy of the encryption-key which will be added to each encrypted backup._ |
| `maxfiles` | integer | False | default | _Maximal number of backup files per VM. Use '0' for unlimted._ |
| `mkdir` | boolean | False | default | _Create the directory if it doesn't exist._ |
| `monhost` | string | False | default | _IP addresses of monitors (for external clusters)._ |
| `mountpoint` | string | False | default | _mount point_ |
| `namespace` | string | False | default | _RBD Namespace._ |
| `nodes` | string | False | default | _List of cluster node names._ |
| `nowritecache` | boolean | False | default | _disable write caching on the target_ |
| `options` | string | False | default | _NFS mount options (see 'man nfs')_ |
| `password` | string | False | True | _Password for accessing the share/datastore._ |
| `pool` | string | False | default | _Pool._ |
| `port` | integer | False | default | _For non default port._ |
| `prune_backups` | string | False | default | _The retention options with shorter intervals are processed first with --keep-last being the very first one. Each option covers a specific period of time. We say that backups within this period are covered by this option. The next option does not take care of already covered backups and only considers older backups._ |
| `redundancy` | integer | False | default | _The redundancy count specifies the number of nodes to which the resource should be deployed. It must be at least 1 and at most the number of nodes in the cluster._ |
| `saferemove` | boolean | False | default | _Zero-out data when removing LVs._ |
| `saferemove_throughput` | string | False | default | _Wipe throughput (cstream -t parameter value)._ |
| `server` | string | False | default | _Server IP or DNS name._ |
| `server2` | string | False | default | _Backup volfile server IP or DNS name._ |
| `shared` | boolean | False | default | _Mark storage as shared._ |
| `smbversion` | string | False | default | _SMB protocol version_ |
| `sparse` | boolean | False | default | _use sparse volumes_ |
| `storage` | string | True | default | _The storage identifier._ |
| `subdir` | string | False | default | _Subdir to mount._ |
| `tagged_only` | boolean | False | default | _Only use logical volumes tagged with 'pve-vm-ID'._ |
| `transport` | string | False | default | _Gluster transport: tcp or rdma_ |
| `username` | string | False | default | _RBD Id._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot_list
_List all snapshots._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_rrddata
_Read VM RRD statistics_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `node` | string | True | default | _The cluster node name._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_reload_network_config
_Reload network configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_aliases_name_read_alias
_Read alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_info
_Get information about node's certificates._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_resources
_Resources index (cluster wide)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_domains_realm_update
_Update authentication server settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `base_dn` | string | False | default | _LDAP base domain name_ |
| `bind_dn` | string | False | default | _LDAP bind domain name_ |
| `capath` | string | False | default | _Path to the CA certificate store_ |
| `case_sensitive` | boolean | False | default | _username is case-sensitive_ |
| `cert` | string | False | default | _Path to the client certificate_ |
| `certkey` | string | False | default | _Path to the client certificate key_ |
| `comment` | string | False | default | _Description._ |
| `default` | boolean | False | default | _Use this as default realm_ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `domain` | string | False | default | _AD domain name_ |
| `prox_filter` | string | False | default | _LDAP filter for user sync._ |
| `group_classes` | string | False | default | _The objectclasses for groups._ |
| `group_dn` | string | False | default | _LDAP base domain name for group sync. If not set, the base_dn will be used._ |
| `group_filter` | string | False | default | _LDAP filter for group sync._ |
| `group_name_attr` | string | False | default | _LDAP attribute representing a groups name. If not set or found, the first value of the DN will be used as name._ |
| `mode` | string | False | default | _LDAP protocol mode._ |
| `password` | string | False | True | _LDAP bind password. Will be stored in '/etc/pve/priv/realm/<REALM>.pw'._ |
| `port` | integer | False | default | _Server port._ |
| `realm` | string | True | default | _Authentication domain ID_ |
| `secure` | boolean | False | default | _Use secure LDAPS protocol. DEPRECATED: use 'mode' instead._ |
| `server1` | string | False | default | _Server IP address (or DNS name)_ |
| `server2` | string | False | default | _Fallback Server IP address (or DNS name)_ |
| `sslversion` | string | False | default | _LDAPS TLS/SSL version. It's not recommended to use version older than 1.2!_ |
| `sync_defaults_options` | string | False | default | _The default options for behavior of synchronizations._ |
| `sync_attributes` | string | False | default | _Comma separated list of key=value pairs for specifying which LDAP attributes map to which PVE user field. For example, to map the LDAP attribute 'mail' to PVEs 'email', write  'email=mail'. By default, each PVE user field is represented  by an LDAP attribute of the same name._ |
| `tfa` | string | False | default | _Use Two-factor authentication._ |
| `user_attr` | string | False | default | _LDAP user attribute name_ |
| `user_classes` | string | False | default | _The objectclasses for users._ |
| `verify` | boolean | False | default | _Verify the server's SSL certificate_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_pending_vm_pending
_Get container configuration, including pending changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_rules_pos_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_initgpt
_Initialize Disk with GPT_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | True | default | _Block device name_ |
| `node` | string | True | default | _The cluster node name._ |
| `uuid` | string | False | default | _UUID for the GPT table_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_pools_createpool
_Create POOL_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storages` | boolean | False | default | _Configure VM and CT storage using the new pool._ |
| `application` | string | False | default | _The application of the pool._ |
| `crush_rule` | string | False | default | _The rule to use for mapping object placement in the cluster._ |
| `min_size` | integer | False | default | _Minimum number of replicas per object_ |
| `name` | string | True | default | _The name of the pool. It must be unique._ |
| `node` | string | True | default | _The cluster node name._ |
| `pg_autoscale_mode` | string | False | default | _The automatic PG scaling mode of the pool._ |
| `pg_num` | integer | False | default | _Number of placement groups._ |
| `pg_num_min` | integer | False | default | _Minimal number of placement groups._ |
| `size` | integer | False | default | _Number of replicas per object_ |
| `target_size` | string | False | default | _The estimated target size of the pool for the PG autoscaler._ |
| `target_size_ratio` | number | False | default | _The estimated target ratio of the pool for the PG autoscaler._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_info
_Execute info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_memory_blocks
_Execute get-memory-blocks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_network_get_interfaces
_Execute network-get-interfaces._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_update
_Update sdn vnet object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `alias` | string | False | default | _alias name of the vnet_ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `tag` | integer | False | default | _vlan or vxlan id_ |
| `vlanaware` | boolean | False | default | _Allow vm VLANs to pass through this vnet._ |
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `zone` | string | False | default | _zone id_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_replication_id_update
_Update replication job configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disable` | boolean | False | default | _Flag to disable/deactivate the entry._ |
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `rate` | number | False | default | _Rate limit in mbps (megabytes per second) as floating point number._ |
| `remove_job` | string | False | default | _Mark the replication job for removal. The job will remove all local replication snapshots. When set to 'full', it also tries to remove replicated volumes on the target. The job then removes itself from the configuration file._ |
| `schedule` | string | False | default | _Storage replication schedule. The format is a subset of `systemd` calendar events._ |
| `source` | string | False | default | _For internal use, to detect if the guest was stolen._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_sid_delete
_Delete resource configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `sid` | string | True | default | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_status_get_status
_Get cluster status information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_name_cidr_update_ip
_Update IP or Network settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `nomatch` | boolean | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_read_user
_Get user configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_usb_usbscan
_List local USB devices._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_zones_zone_delete
_Delete sdn zone object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `zone` | string | True | default | _The SDN zone object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_users
_Execute get-users._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_aliases_create_alias
_Create IP or Network Alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_controllers_controller_delete
_Delete sdn controller object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `controller` | string | True | default | _The SDN controller object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_tasks
_List recent tasks (cluster wide)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_domains_create
_Add an authentication server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `base_dn` | string | False | default | _LDAP base domain name_ |
| `bind_dn` | string | False | default | _LDAP bind domain name_ |
| `capath` | string | False | default | _Path to the CA certificate store_ |
| `case_sensitive` | boolean | False | default | _username is case-sensitive_ |
| `cert` | string | False | default | _Path to the client certificate_ |
| `certkey` | string | False | default | _Path to the client certificate key_ |
| `comment` | string | False | default | _Description._ |
| `default` | boolean | False | default | _Use this as default realm_ |
| `domain` | string | False | default | _AD domain name_ |
| `prox_filter` | string | False | default | _LDAP filter for user sync._ |
| `group_classes` | string | False | default | _The objectclasses for groups._ |
| `group_dn` | string | False | default | _LDAP base domain name for group sync. If not set, the base_dn will be used._ |
| `group_filter` | string | False | default | _LDAP filter for group sync._ |
| `group_name_attr` | string | False | default | _LDAP attribute representing a groups name. If not set or found, the first value of the DN will be used as name._ |
| `mode` | string | False | default | _LDAP protocol mode._ |
| `password` | string | False | True | _LDAP bind password. Will be stored in '/etc/pve/priv/realm/<REALM>.pw'._ |
| `port` | integer | False | default | _Server port._ |
| `realm` | string | True | default | _Authentication domain ID_ |
| `secure` | boolean | False | default | _Use secure LDAPS protocol. DEPRECATED: use 'mode' instead._ |
| `server1` | string | False | default | _Server IP address (or DNS name)_ |
| `server2` | string | False | default | _Fallback Server IP address (or DNS name)_ |
| `sslversion` | string | False | default | _LDAPS TLS/SSL version. It's not recommended to use version older than 1.2!_ |
| `sync_defaults_options` | string | False | default | _The default options for behavior of synchronizations._ |
| `sync_attributes` | string | False | default | _Comma separated list of key=value pairs for specifying which LDAP attributes map to which PVE user field. For example, to map the LDAP attribute 'mail' to PVEs 'email', write  'email=mail'. By default, each PVE user field is represented  by an LDAP attribute of the same name._ |
| `tfa` | string | False | default | _Use Two-factor authentication._ |
| `prox_type` | string | True | default | _Realm type._ |
| `user_attr` | string | False | default | _LDAP user attribute name_ |
| `user_classes` | string | False | default | _The objectclasses for users._ |
| `verify` | boolean | False | default | _Verify the server's SSL certificate_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_prunebackups_delete
_Prune backups. Only those using the standard naming scheme are considered._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prune_backups` | string | False | default | _Use these retention options instead of those from the storage configuration._ |
| `storage` | string | True | default | _The storage identifier._ |
| `prox_type` | string | False | default | _Either 'qemu' or 'lxc'. Only consider backups for guests of this type._ |
| `vmid` | integer | False | default | _Only prune backups for this VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_zones_zone_read
_Read sdn zone configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `zone` | string | True | default | _The SDN zone object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_pools_name_setpool
_Change POOL settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `application` | string | False | default | _The application of the pool._ |
| `crush_rule` | string | False | default | _The rule to use for mapping object placement in the cluster._ |
| `min_size` | integer | False | default | _Minimum number of replicas per object_ |
| `name` | string | True | default | _The name of the pool. It must be unique._ |
| `node` | string | True | default | _The cluster node name._ |
| `pg_autoscale_mode` | string | False | default | _The automatic PG scaling mode of the pool._ |
| `pg_num` | integer | False | default | _Number of placement groups._ |
| `pg_num_min` | integer | False | default | _Minimal number of placement groups._ |
| `size` | integer | False | default | _Number of replicas per object_ |
| `target_size` | string | False | default | _The estimated target size of the pool for the PG autoscaler._ |
| `target_size_ratio` | number | False | default | _The estimated target ratio of the pool for the PG autoscaler._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_content_volume_info
_Get volume attributes_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | False | default | _The storage identifier._ |
| `volume` | string | True | default | _Volume identifier_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_stop
_Stop ceph services._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | False | default | _Ceph service name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_groups_create
_Create a new HA group._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description._ |
| `group` | string | True | default | _The HA group identifier._ |
| `nodes` | string | True | default | _List of cluster node names with optional priority._ |
| `nofailback` | boolean | False | default | _The CRM tries to run services on the node with the highest priority. If a node with higher priority comes online, the CRM migrates the service to that node. Enabling nofailback prevents that behavior._ |
| `restricted` | boolean | False | default | _Resources bound to restricted groups may only run on nodes defined by the group._ |
| `prox_type` | string | False | default | _Group type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_metrics_index
_Metrics index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backup_id_delete_job
_Delete vzdump backup job definition._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _The job ID._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### storage_storage_read
_Read storage configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `storage` | string | True | default | _The storage identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_group_get_rules
_List rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | default | _Security Group name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_reload
_Apply sdn controller changes && reload._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_sdn_sdnindex
_SDN index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_suspend_hybrid
_Execute suspend-hybrid._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_sid_read
_Read resource configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `sid` | string | True | default | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_qdevice_status
_Get QDevice status_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_subscription_get
_Read subscription info._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dhcp` | boolean | False | default | _Enable DHCP._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `enable` | boolean | False | default | _Enable/disable firewall rules._ |
| `ipfilter` | boolean | False | default | _Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added._ |
| `log_level_in` | string | False | default | _Log level for incoming traffic._ |
| `log_level_out` | string | False | default | _Log level for outgoing traffic._ |
| `macfilter` | boolean | False | default | _Enable/disable MAC address filter._ |
| `ndp` | boolean | False | default | _Enable NDP (Neighbor Discovery Protocol)._ |
| `node` | string | True | default | _The cluster node name._ |
| `policy_in` | string | False | default | _Input policy._ |
| `policy_out` | string | False | default | _Output policy._ |
| `radv` | boolean | False | default | _Allow sending Router Advertisement._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backup_id_update_job
_Update vzdump backup job definition._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_all` | boolean | False | default | _Backup all known guest systems on this host._ |
| `bwlimit` | integer | False | default | _Limit I/O bandwidth (KBytes per second)._ |
| `compress` | string | False | default | _Compress dump file._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dow` | string | False | default | _Day of week selection._ |
| `dumpdir` | string | False | default | _Store resulting files to specified directory._ |
| `enabled` | boolean | False | default | _Enable or disable the job._ |
| `exclude` | string | False | default | _Exclude specified guest systems (assumes --all)_ |
| `exclude_path` | string | False | default | _Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root,  other paths match relative to each subdirectory._ |
| `prox_id` | string | True | default | _The job ID._ |
| `ionice` | integer | False | default | _Set CFQ ionice priority._ |
| `lockwait` | integer | False | default | _Maximal time to wait for the global lock (minutes)._ |
| `mailnotification` | string | False | default | _Specify when to send an email_ |
| `mailto` | string | False | default | _Comma-separated list of email addresses or users that should receive email notifications._ |
| `maxfiles` | integer | False | default | _Maximal number of backup files per guest system._ |
| `mode` | string | False | default | _Backup mode._ |
| `node` | string | False | default | _Only run if executed on this node._ |
| `pigz` | integer | False | default | _Use pigz instead of gzip when N>0. N=1 uses half of cores, N>1 uses N as thread count._ |
| `pool` | string | False | default | _Backup all known guest systems included in the specified pool._ |
| `prune_backups` | string | False | default | _Use these retention options instead of those from the storage configuration._ |
| `quiet` | boolean | False | default | _Be quiet._ |
| `remove` | boolean | False | default | _Remove old backup files if there are more than 'maxfiles' backup files._ |
| `script` | string | False | default | _Use specified hook script._ |
| `size` | integer | False | default | _Unused, will be removed in a future release._ |
| `starttime` | string | True | default | _Job Start time._ |
| `stdexcludes` | boolean | False | default | _Exclude temporary files and logs._ |
| `stop` | boolean | False | default | _Stop running backup jobs on this host._ |
| `stopwait` | integer | False | default | _Maximal time to wait until a guest system is stopped (minutes)._ |
| `storage` | string | False | default | _Store resulting file to this storage._ |
| `tmpdir` | string | False | default | _Store temporary files to specified directory._ |
| `vmid` | string | False | default | _The ID of the guest system you want to backup._ |
| `zstd` | integer | False | default | _Zstd threads. N=0 uses half of the available cores, N>0 uses N as thread count._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_cloudinit_dump_cloudinit_generated_config_dump
_Get automatically generated cloudinit config._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prox_type` | string | True | default | _Config type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_service_start
_Start service._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | True | default | _Service ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hosts_write_etc_hosts
_Write /etc/hosts._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `data` | string | True | default | _The target content of /etc/hosts._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mon_monid_destroymon
_Destroy Ceph Monitor and Manager._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `monid` | string | True | default | _Monitor ID_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_groups_index
_Get HA groups._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_rules_create_rule
_Create new rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | True | default | _Rule type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_dns_dns_delete
_Delete sdn dns object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns` | string | True | default | _The SDN dns object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backup_index
_List vzdump backup schedule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_config_set_options
_Set node configuration options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acme` | string | False | default | _Node specific ACME settings._ |
| `acmedomain_list` | string | False | default | _ACME domain and validation plugin_ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `description` | string | False | default | _Node description/comment._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | default | _The cluster node name._ |
| `startall_onboot_delay` | integer | False | default | _Initial delay in seconds, before starting all the Virtual Guests with on-boot enabled._ |
| `wakeonlan` | string | False | default | _MAC address for wake on LAN_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_subnets_index
_SDN subnets index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `pending` | boolean | False | default | _Display pending config._ |
| `running` | boolean | False | default | _Display running config._ |
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_lvmthin_create
_Create an LVM thinpool_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | default | _Configure storage using the thinpool._ |
| `device` | string | True | default | _The block device you want to create the thinpool on._ |
| `name` | string | True | default | _The storage identifier._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_file_read
_Reads the given file via guest agent. Is limited to 16777216 bytes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `file` | string | True | default | _The path to the file_ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_rules_pos_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `moveto` | integer | False | default | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | False | default | _Rule type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_content_volume_copy
_Copy a volume. This is experimental code - do not use._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | False | default | _The storage identifier._ |
| `target` | string | True | default | _Target volume identifier_ |
| `target_node` | string | False | default | _Target node. Default is local node._ |
| `volume` | string | True | default | _Source volume identifier_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_status_stop_vm_stop
_Stop the container. This will abruptly stop all processes running in the container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_vzdump
_Create backup._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_all` | boolean | False | default | _Backup all known guest systems on this host._ |
| `bwlimit` | integer | False | default | _Limit I/O bandwidth (KBytes per second)._ |
| `compress` | string | False | default | _Compress dump file._ |
| `dumpdir` | string | False | default | _Store resulting files to specified directory._ |
| `exclude` | string | False | default | _Exclude specified guest systems (assumes --all)_ |
| `exclude_path` | string | False | default | _Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root,  other paths match relative to each subdirectory._ |
| `ionice` | integer | False | default | _Set CFQ ionice priority._ |
| `lockwait` | integer | False | default | _Maximal time to wait for the global lock (minutes)._ |
| `mailnotification` | string | False | default | _Specify when to send an email_ |
| `mailto` | string | False | default | _Comma-separated list of email addresses or users that should receive email notifications._ |
| `maxfiles` | integer | False | default | _Maximal number of backup files per guest system._ |
| `mode` | string | False | default | _Backup mode._ |
| `node` | string | False | default | _Only run if executed on this node._ |
| `pigz` | integer | False | default | _Use pigz instead of gzip when N>0. N=1 uses half of cores, N>1 uses N as thread count._ |
| `pool` | string | False | default | _Backup all known guest systems included in the specified pool._ |
| `prune_backups` | string | False | default | _Use these retention options instead of those from the storage configuration._ |
| `quiet` | boolean | False | default | _Be quiet._ |
| `remove` | boolean | False | default | _Remove old backup files if there are more than 'maxfiles' backup files._ |
| `script` | string | False | default | _Use specified hook script._ |
| `size` | integer | False | default | _Unused, will be removed in a future release._ |
| `stdexcludes` | boolean | False | default | _Exclude temporary files and logs._ |
| `stdout` | boolean | False | default | _Write tar to stdout, not to a file._ |
| `stop` | boolean | False | default | _Stop running backup jobs on this host._ |
| `stopwait` | integer | False | default | _Maximal time to wait until a guest system is stopped (minutes)._ |
| `storage` | string | False | default | _Store resulting file to this storage._ |
| `tmpdir` | string | False | default | _Store temporary files to specified directory._ |
| `vmid` | string | False | default | _The ID of the guest system you want to backup._ |
| `zstd` | integer | False | default | _Zstd threads. N=0 uses half of the available cores, N>0 uses N as thread count._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_permissions
_Retrieve effective permissions of given user/token._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `path` | string | False | default | _Only dump this specific path, not the whole tree._ |
| `userid` | string | False | default | _User ID or full API token ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_zfs_index
_List Zpools._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_content_index
_List storage content._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `content` | string | False | default | _Only list content of this type._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `vmid` | integer | False | default | _Only list images for this VM_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_sid_migrate
_Request resource migration (online) to another node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _Target node._ |
| `sid` | string | True | default | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hardware_pci_pciid_pciindex
_Index of available pci methods_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pciid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot_snapname_config_get_snapshot_config
_Get snapshot configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backup_id_read_job
_Read vzdump backup job definition._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _The job ID._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_rules_create_rule
_Create new rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | True | default | _Rule type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_vncproxy
_Creates a TCP VNC proxy connections._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `height` | integer | False | default | _sets the height of the console in pixels._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `websocket` | boolean | False | default | _use websocket instead of standard VNC._ |
| `width` | integer | False | default | _sets the width of the console in pixels._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_suspend_vm_suspend
_Suspend virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `statestorage` | string | False | default | _The storage for the VM state_ |
| `todisk` | boolean | False | default | _If set, suspends the VM to disk. Will be resumed on next VM start._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_vncproxy
_Creates a TCP VNC proxy connections._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `generate_password` | boolean | False | default | _Generates a random password to be used as ticket instead of the API ticket._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `websocket` | boolean | False | default | _starts websockify instead of vncproxy_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_groups_group_delete
_Delete ha group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | default | _The HA group identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mgr_id_createmgr
_Create Ceph Manager_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | False | default | _The ID for the manager, when omitted the same as the nodename_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_status
_Get ceph status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_subscription_delete
_Delete subscription key of this node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot_snapname_snapshot_cmd_idx
__

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_rules_pos_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `moveto` | integer | False | default | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | False | default | _Rule type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_log
_Read ceph log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `start` | integer | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_token_token_index
_Get user API tokens._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_shutdown_vm_shutdown
_Shutdown virtual machine. This is similar to pressing the power button on a physical machine.This will send an ACPI event for the guest OS, which should then proceed to a clean shutdown._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `forceStop` | boolean | False | default | _Make sure the VM stops._ |
| `keepActive` | boolean | False | default | _Do not deactivate storage volumes._ |
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `timeout` | integer | False | default | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_join
_Joins this node into an existing cluster. If no links are given, default to IP resolved by node's hostname on single link (fallback fails for clusters with multiple links)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `fingerprint` | string | True | default | _Certificate SHA 256 fingerprint._ |
| `force` | boolean | False | default | _Do not throw error if node already exists._ |
| `hostname` | string | True | default | _Hostname (or IP) of an existing cluster member._ |
| `link_list` | string | False | default | _Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)_ |
| `nodeid` | integer | False | default | _Node id for this node._ |
| `password` | string | True | True | _Superuser (root) password of peer node._ |
| `votes` | integer | False | default | _Number of votes for this node_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_revert_network_changes
_Revert network configuration changes._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_aliases_name_read_alias
_Read alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _Alias name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_plugins_add_plugin
_Add ACME plugin configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api` | string | False | default | _API plugin name_ |
| `data` | string | False | default | _DNS plugin data. (base64 encoded)_ |
| `disable` | boolean | False | default | _Flag to disable the config._ |
| `prox_id` | string | True | default | _ACME Plugin ID name_ |
| `nodes` | string | False | default | _List of cluster node names._ |
| `prox_type` | string | True | default | _ACME challenge type._ |
| `validation_delay` | integer | False | default | _Extra delay in seconds to wait before requesting validation. Allows to cope with a long TTL of DNS records._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_osd_index
_Get Ceph osd list/tree._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### pools_poolid_update_pool
_Update pool data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `delete` | boolean | False | default | _Remove vms/storage (instead of adding it)._ |
| `poolid` | string | True | default | _Description unavailable._ |
| `storage` | string | False | default | _List of storage IDs._ |
| `vms` | string | False | default | _List of virtual machines._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### pools_create_pool
_Create new pool._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `poolid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_osd_osdid_out
_ceph osd out_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `osdid` | integer | True | default | _OSD ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_vzdump_extractconfig
_Extract configuration from vzdump backup archive._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `volume` | string | True | default | _Volume identifier_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_journal
_Read Journal_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `endcursor` | string | False | default | _End before the given Cursor. Conflicts with 'until'_ |
| `lastentries` | integer | False | default | _Limit to the last X lines. Conflicts with a range._ |
| `node` | string | True | default | _The cluster node name._ |
| `since` | integer | False | default | _Display all log since this UNIX epoch. Conflicts with 'startcursor'._ |
| `startcursor` | string | False | default | _Start after the given Cursor. Conflicts with 'since'_ |
| `until` | integer | False | default | _Display all log until this UNIX epoch. Conflicts with 'endcursor'._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_stopall
_Stop all VMs and Containers._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vms` | string | False | default | _Only consider Guests with these IDs._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_resize_resize_vm
_Resize a container mount point._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disk` | string | True | default | _The disk you want to resize._ |
| `node` | string | True | default | _The cluster node name._ |
| `size` | string | True | default | _The new size. With the '+' sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_nodes_node_delnode
_Removes a node from the cluster configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_time_set_timezone
_Set time zone._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `timezone` | string | True | default | _Time zone. The file '/usr/share/zoneinfo/zone.tab' contains the list of valid names._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_fsinfo
_Execute get-fsinfo._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_apt_update_update_database
_This is used to resynchronize the package index files from their sources (apt-get update)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `notify` | boolean | False | default | _Send notification mail about new packages (to email address specified for user 'root@pam')._ |
| `quiet` | boolean | False | default | _Only produces output suitable for logging, omitting progress indicators._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_services_service_state
_Read service properties_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | True | default | _Service ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_index
_Node index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_vncwebsocket
_Opens a weksocket for VNC traffic._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `port` | integer | True | default | _Port number returned by previous vncproxy call._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `vncticket` | string | True | default | _Ticket from previous call to vncproxy._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_lvm_index
_List LVM Volume Groups_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_iscsi_iscsiscan
_Scan remote iSCSI server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `portal` | string | True | default | _The iSCSI portal (IP or DNS name with optional port)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_ipset_index
_List IPSets_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_tos_get_tos
_Retrieve ACME TermsOfService URL from CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `directory` | string | False | default | _URL of ACME CA directory endpoint._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_rules_get_rules
_List rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_options_set_options
_Set datacenter options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | string | False | default | _Set bandwidth/io limits various operations._ |
| `console` | string | False | default | _Select the default Console viewer. You can either use the builtin java applet (VNC; deprecated and maps to html5), an external virt-viewer comtatible application (SPICE), an HTML5 based vnc viewer (noVNC), or an HTML5 based console client (xtermjs). If the selected viewer is not available (e.g. SPICE not activated for the VM), the fallback is noVNC._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `email_from` | string | False | default | _Specify email address to send notification from (default is root@$hostname)_ |
| `fencing` | string | False | default | _Set the fencing mode of the HA cluster. Hardware mode needs a valid configuration of fence devices in /etc/pve/ha/fence.cfg. With both all two modes are used.  WARNING: 'hardware' and 'both' are EXPERIMENTAL & WIP_ |
| `ha` | string | False | default | _Cluster wide HA settings._ |
| `http_proxy` | string | False | default | _Specify external http proxy which is used for downloads (example: 'http://username:password@host:port/')_ |
| `keyboard` | string | False | default | _Default keybord layout for vnc server._ |
| `language` | string | False | default | _Default GUI language._ |
| `mac_prefix` | string | False | default | _Prefix for autogenerated MAC addresses._ |
| `max_workers` | integer | False | default | _Defines how many workers (per node) are maximal started  on actions like 'stopall VMs' or task from the ha-manager._ |
| `migration` | string | False | default | _For cluster wide migration settings._ |
| `migration_unsecure` | boolean | False | default | _Migration is secure using SSH tunnel by default. For secure private networks you can disable it to speed up migration. Deprecated, use the 'migration' property instead!_ |
| `u2f` | string | False | default | _u2f_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_suspend_disk
_Execute suspend-disk._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_tasks_upid_stop_task
_Stop a task._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `upid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_config
_Get Ceph configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hardware_usb_usbscan
_List local USB devices._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_lvm_lvmscan
_List local LVM volume groups._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_ipams_create
_Create a new sdn ipam object._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `ipam` | string | True | default | _The SDN ipam object identifier._ |
| `section` | integer | False | default | _Description unavailable._ |
| `token` | string | False | default | _Description unavailable._ |
| `prox_type` | string | True | default | _Plugin type._ |
| `url` | string | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_aliases_name_update_alias
_Update IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _Alias name._ |
| `rename` | string | False | default | _Rename an existing alias._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_group_pos_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `group` | string | True | default | _Security Group name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_status
_Read node status_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_token_tokenid_update_token_info
_Update API token for a specific user._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `expire` | integer | False | default | _API token expiration date (seconds since epoch). '0' means no expiration date._ |
| `privsep` | boolean | False | default | _Restrict API token privileges with separate ACLs (default), or give full privileges of corresponding user._ |
| `tokenid` | string | True | default | _User-specific token identifier._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_set_user_password
_Sets the password for the given user to the given password_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `crypted` | boolean | False | default | _set to 1 if the password has already been passed through crypt()_ |
| `node` | string | True | default | _The cluster node name._ |
| `password` | string | True | True | _The new password._ |
| `username` | string | True | default | _The user to set the password for._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_aliases_name_update_alias
_Update IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `rename` | string | False | default | _Rename an existing alias._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_ipams_ipam_read
_Read sdn ipam configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `ipam` | string | True | default | _The SDN ipam object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_options_get_options
_Get host firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_create_ipset
_Create new IPSet_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `rename` | string | False | default | _Rename an existing IPSet. You can set 'rename' to the same value as 'name' to update the 'comment' of an existing IPSet._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_metrics_server_id_create
_Create a new external metric server config_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `api_path_prefix` | string | False | default | _An API path prefix inserted between '<host>:<port>/' and '/api2/'. Can be useful if the InfluxDB service runs behind a reverse proxy._ |
| `bucket` | string | False | default | _The InfluxDB bucket/db. Only necessary when using the http v2 api._ |
| `disable` | boolean | False | default | _Flag to disable the plugin._ |
| `prox_id` | string | True | default | _The ID of the entry._ |
| `influxdbproto` | string | False | default | _Description unavailable._ |
| `max_body_size` | integer | False | default | _InfluxDB max-body-size in bytes. Requests are batched up to this size._ |
| `mtu` | integer | False | default | _MTU for metrics transmission over UDP_ |
| `organization` | string | False | default | _The InfluxDB organization. Only necessary when using the http v2 api. Has no meaning when using v2 compatibility api._ |
| `path` | string | False | default | _root graphite path (ex: proxmox.mycluster.mykey)_ |
| `port` | integer | True | default | _server network port_ |
| `proto` | string | False | default | _Protocol to send graphite data. TCP or UDP (default)_ |
| `server` | string | True | default | _server dns name or IP address_ |
| `timeout` | integer | False | default | _graphite TCP socket timeout (default=1)_ |
| `token` | string | False | default | _The InfluxDB access token. Only necessary when using the http v2 api. If the v2 compatibility api is used, use 'user:password' instead._ |
| `prox_type` | string | True | default | _Plugin type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_vmcmdidx
_Directory index_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_replication_id_schedule_now
_Schedule replication job to start as soon as possible._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_log
_Read firewall log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `start` | integer | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_rrddata
_Read storage RRD statistics._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_name_create_ip
_Add IP or Network to IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `nomatch` | boolean | False | default | _Description unavailable._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_dns
_Read DNS settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_index
_Get status for all datastores._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `content` | string | False | default | _Only list stores which support this content type._ |
| `enabled` | boolean | False | default | _Only list stores which are enabled (not disabled in config)._ |
| `prox_format` | boolean | False | default | _Include information about formats_ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | False | default | _Only list status for  specified storage_ |
| `target` | string | False | default | _If target is different to 'node', we only lists shared storages which content is accessible on this 'node' and the specified 'target' node._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_delete
_Delete sdn vnet object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `vnet` | string | True | default | _The SDN vnet object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_destroy_vm
_Destroy the VM and  all used/owned volumes. Removes any VM specific permissions and firewall rules_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `destroy_unreferenced_disks` | boolean | False | default | _If set, destroy additionally all disks not referenced in the config but with a matching VMID from all enabled storages._ |
| `node` | string | True | default | _The cluster node name._ |
| `purge` | boolean | False | default | _Remove VMID from configurations, like backup & replication jobs and HA._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_config_get_config
_Get node configuration options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prox_property` | string | False | default | _Return only a specific property from the node configuration._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_create_vm
_Create or restore a virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acpi` | boolean | False | default | _Enable/disable ACPI._ |
| `agent` | string | False | default | _Enable/disable Qemu GuestAgent and its properties._ |
| `arch` | string | False | default | _Virtual processor architecture. Defaults to the host._ |
| `archive` | string | False | default | _The backup archive. Either the file system path to a .tar or .vma file (use '-' to pipe data from stdin) or a proxmox storage backup volume identifier._ |
| `args` | string | False | default | _Arbitrary arguments passed to kvm._ |
| `audio0` | string | False | default | _Configure a audio device, useful in combination with QXL/Spice._ |
| `autostart` | boolean | False | default | _Automatic restart after crash (currently ignored)._ |
| `balloon` | integer | False | default | _Amount of target RAM for the VM in MB. Using zero disables the ballon driver._ |
| `bios` | string | False | default | _Select BIOS implementation._ |
| `boot` | string | False | default | _Specify guest boot order. Use with 'order=', usage with no key or 'legacy=' is deprecated._ |
| `bootdisk` | string | False | default | _Enable booting from specified disk. Deprecated: Use 'boot: order=foo;bar' instead._ |
| `bwlimit` | integer | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `cdrom` | string | False | default | _This is an alias for option -ide2_ |
| `cicustom` | string | False | default | _cloud-init: Specify custom files to replace the automatically generated ones at start._ |
| `cipassword` | string | False | default | _cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords._ |
| `citype` | string | False | default | _Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows._ |
| `ciuser` | string | False | default | _cloud-init: User name to change ssh keys and password for instead of the image's configured default user._ |
| `cores` | integer | False | default | _The number of cores per socket._ |
| `cpu` | string | False | default | _Emulated CPU type._ |
| `cpulimit` | number | False | default | _Limit of CPU usage._ |
| `cpuunits` | integer | False | default | _CPU weight for a VM._ |
| `description` | string | False | default | _Description for the VM. Only used on the configuration web interface. This is saved as comment inside the configuration file._ |
| `efidisk0` | string | False | default | _Configure a Disk for storing EFI vars. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume. Note that SIZE_IN_GiB is ignored here and that the default EFI vars are copied to the volume instead._ |
| `force` | boolean | False | default | _Allow to overwrite existing VM._ |
| `freeze` | boolean | False | default | _Freeze CPU at startup (use 'c' monitor command to start execution)._ |
| `hookscript` | string | False | default | _Script that will be executed during various steps in the vms lifetime._ |
| `hostpci_list` | string | False | default | _Map host PCI devices into guest._ |
| `hotplug` | string | False | default | _Selectively enable hotplug features. This is a comma separated list of hotplug features: 'network', 'disk', 'cpu', 'memory' and 'usb'. Use '0' to disable hotplug completely. Value '1' is an alias for the default 'network,disk,usb'._ |
| `hugepages` | string | False | default | _Enable/disable hugepages memory._ |
| `ide_list` | string | False | default | _Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `ipconfig_list` | string | False | default | _cloud-init: Specify IP addresses and gateways for the corresponding interface.  IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.  The special string 'dhcp' can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string 'auto' can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.  If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4. _ |
| `ivshmem` | string | False | default | _Inter-VM shared memory. Useful for direct communication between VMs, or to the host._ |
| `keephugepages` | boolean | False | default | _Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts._ |
| `keyboard` | string | False | default | _Keybord layout for vnc server. Default is read from the '/etc/pve/datacenter.cfg' configuration file.It should not be necessary to set it._ |
| `kvm` | boolean | False | default | _Enable/disable KVM hardware virtualization._ |
| `live_restore` | boolean | False | default | _Start the VM immediately from the backup and restore in background. PBS only._ |
| `localtime` | boolean | False | default | _Set the real time clock to local time. This is enabled by default if ostype indicates a Microsoft OS._ |
| `lock` | string | False | default | _Lock/unlock the VM._ |
| `machine` | string | False | default | _Specifies the Qemu machine type._ |
| `memory` | integer | False | default | _Amount of RAM for the VM in MB. This is the maximum available memory when you use the balloon device._ |
| `migrate_downtime` | number | False | default | _Set maximum tolerated downtime (in seconds) for migrations._ |
| `migrate_speed` | integer | False | default | _Set maximum speed (in MB/s) for migrations. Value 0 is no limit._ |
| `name` | string | False | default | _Set a name for the VM. Only used on the configuration web interface._ |
| `nameserver` | string | False | default | _cloud-init: Sets DNS server IP address for a container. Create will'     .' automatically use the setting from the host if neither searchdomain nor nameserver'     .' are set._ |
| `net_list` | string | False | default | _Specify network devices._ |
| `node` | string | True | default | _The cluster node name._ |
| `numa` | boolean | False | default | _Enable/disable NUMA._ |
| `numa_list` | string | False | default | _NUMA topology._ |
| `onboot` | boolean | False | default | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | default | _Specify guest operating system._ |
| `parallel_list` | string | False | default | _Map host parallel devices (n is 0 to 2)._ |
| `pool` | string | False | default | _Add the VM to the specified pool._ |
| `protection` | boolean | False | default | _Sets the protection flag of the VM. This will disable the remove VM and remove disk operations._ |
| `reboot` | boolean | False | default | _Allow reboot. If set to '0' the VM exit on reboot._ |
| `rng0` | string | False | default | _Configure a VirtIO-based Random Number Generator._ |
| `sata_list` | string | False | default | _Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsi_list` | string | False | default | _Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsihw` | string | False | default | _SCSI controller model_ |
| `searchdomain` | string | False | default | _cloud-init: Sets DNS search domains for a container. Create will'     .' automatically use the setting from the host if neither searchdomain nor nameserver'     .' are set._ |
| `serial_list` | string | False | default | _Create a serial device inside the VM (n is 0 to 3)_ |
| `shares` | integer | False | default | _Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd._ |
| `smbios1` | string | False | default | _Specify SMBIOS type 1 fields._ |
| `smp` | integer | False | default | _The number of CPUs. Please use option -sockets instead._ |
| `sockets` | integer | False | default | _The number of CPU sockets._ |
| `spice_enhancements` | string | False | default | _Configure additional enhancements for SPICE._ |
| `sshkeys` | string | False | default | _cloud-init: Setup public SSH keys (one key per line, OpenSSH format)._ |
| `start` | boolean | False | default | _Start VM after it was created successfully._ |
| `startdate` | string | False | default | _Set the initial date of the real time clock. Valid format for date are:'now' or '2006-06-17T16:01:21' or '2006-06-17'._ |
| `startup` | string | False | default | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `storage` | string | False | default | _Default storage._ |
| `tablet` | boolean | False | default | _Enable/disable the USB tablet device._ |
| `tags` | string | False | default | _Tags of the VM. This is only meta information._ |
| `tdf` | boolean | False | default | _Enable/disable time drift fix._ |
| `template` | boolean | False | default | _Enable/disable Template._ |
| `unique` | boolean | False | default | _Assign a unique random ethernet address._ |
| `unused_list` | string | False | default | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `usb_list` | string | False | default | _Configure an USB device (n is 0 to 4)._ |
| `vcpus` | integer | False | default | _Number of hotplugged vcpus._ |
| `vga` | string | False | default | _Configure the VGA hardware._ |
| `virtio_list` | string | False | default | _Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `vmgenid` | string | False | default | _Set VM Generation ID. Use '1' to autogenerate on create or update, pass '0' to disable explicitly._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `vmstatestorage` | string | False | default | _Default storage for VM state volumes/files._ |
| `watchdog` | string | False | default | _Create a virtual hardware watchdog device._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mds_name_destroymds
_Destroy Ceph Metadata Server_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _The name (ID) of the mds_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_pools_lspools
_List all pools._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_groups_groupid_delete_group
_Delete group._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `groupid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_directory_index
_PVE Managed Directory storages._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_groups_group_update
_Update ha group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `group` | string | True | default | _The HA group identifier._ |
| `nodes` | string | False | default | _List of cluster node names with optional priority._ |
| `nofailback` | boolean | False | default | _The CRM tries to run services on the node with the highest priority. If a node with higher priority comes online, the CRM migrates the service to that node. Enabling nofailback prevents that behavior._ |
| `restricted` | boolean | False | default | _Resources bound to restricted groups may only run on nodes defined by the group._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_monitor
_Execute Qemu monitor commands._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `command` | string | True | default | _The monitor command._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_name_cidr_read_ip
_Read IP or Network settings from IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_iface_delete_network
_Delete network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `iface` | string | True | default | _Network interface name._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_rules_get_rules
_List rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_apt_index
_Directory index for apt (Advanced Package Tool)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_capabilities_index
_Node capabilities index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_update_user
_Update user configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `append` | boolean | False | default | _Description unavailable._ |
| `comment` | string | False | default | _Description unavailable._ |
| `email` | string | False | default | _Description unavailable._ |
| `enable` | boolean | False | default | _Enable the account (default). You can set this to '0' to disable the account_ |
| `expire` | integer | False | default | _Account expiration date (seconds since epoch). '0' means no expiration date._ |
| `firstname` | string | False | default | _Description unavailable._ |
| `groups` | string | False | default | _Description unavailable._ |
| `keys` | string | False | default | _Keys for two factor auth (yubico)._ |
| `lastname` | string | False | default | _Description unavailable._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_acme_certificate_renew_certificate
_Renew existing certificate from CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _Force renewal even if expiry is more than 30 days away._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_options_get_options
_Get VM firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_aliases_create_alias
_Create IP or Network Alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_mds_index
_MDS directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_flags_get_flags
_get all set ceph flags_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_fs_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_acl_read_acl
_Get Access Control List (ACLs)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_zfs_name_detail
_Get details about a zpool._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _The storage identifier._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_current_vm_status
_Get virtual machine status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_groups_create_group
_Create new group._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `groupid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot_snapname_rollback
_Rollback VM state to specified snapshot._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_content_create
_Allocate disk images._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `filename` | string | True | default | _The name of the file to create._ |
| `prox_format` | string | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `size` | string | True | default | _Size in kilobyte (1024 bytes). Optional suffixes 'M' (megabyte, 1024K) and 'G' (gigabyte, 1024M)_ |
| `storage` | string | True | default | _The storage identifier._ |
| `vmid` | integer | True | default | _Specify owner VM_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_clone_clone_vm
_Create a container clone/copy_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | number | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `description` | string | False | default | _Description for the new CT._ |
| `full` | boolean | False | default | _Create a full copy of all disks. This is always done when you clone a normal CT. For CT templates, we try to create a linked clone by default._ |
| `hostname` | string | False | default | _Set a hostname for the new CT._ |
| `newid` | integer | True | default | _VMID for the clone._ |
| `node` | string | True | default | _The cluster node name._ |
| `pool` | string | False | default | _Add the new CT to the specified pool._ |
| `snapname` | string | False | default | _The name of the snapshot._ |
| `storage` | string | False | default | _Target storage for full clone._ |
| `target` | string | False | default | _Target node. Only allowed if the original VM is on shared storage._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_userid_token_tokenid_read_token
_Get specific API token information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `tokenid` | string | True | default | _User-specific token identifier._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_config_update_vm
_Set virtual machine options (synchrounous API) - You should consider using the POST method instead for any actions involving hotplug or storage allocation._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acpi` | boolean | False | default | _Enable/disable ACPI._ |
| `agent` | string | False | default | _Enable/disable Qemu GuestAgent and its properties._ |
| `arch` | string | False | default | _Virtual processor architecture. Defaults to the host._ |
| `args` | string | False | default | _Arbitrary arguments passed to kvm._ |
| `audio0` | string | False | default | _Configure a audio device, useful in combination with QXL/Spice._ |
| `autostart` | boolean | False | default | _Automatic restart after crash (currently ignored)._ |
| `balloon` | integer | False | default | _Amount of target RAM for the VM in MB. Using zero disables the ballon driver._ |
| `bios` | string | False | default | _Select BIOS implementation._ |
| `boot` | string | False | default | _Specify guest boot order. Use with 'order=', usage with no key or 'legacy=' is deprecated._ |
| `bootdisk` | string | False | default | _Enable booting from specified disk. Deprecated: Use 'boot: order=foo;bar' instead._ |
| `cdrom` | string | False | default | _This is an alias for option -ide2_ |
| `cicustom` | string | False | default | _cloud-init: Specify custom files to replace the automatically generated ones at start._ |
| `cipassword` | string | False | default | _cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords._ |
| `citype` | string | False | default | _Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows._ |
| `ciuser` | string | False | default | _cloud-init: User name to change ssh keys and password for instead of the image's configured default user._ |
| `cores` | integer | False | default | _The number of cores per socket._ |
| `cpu` | string | False | default | _Emulated CPU type._ |
| `cpulimit` | number | False | default | _Limit of CPU usage._ |
| `cpuunits` | integer | False | default | _CPU weight for a VM._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `description` | string | False | default | _Description for the VM. Only used on the configuration web interface. This is saved as comment inside the configuration file._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `efidisk0` | string | False | default | _Configure a Disk for storing EFI vars. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume. Note that SIZE_IN_GiB is ignored here and that the default EFI vars are copied to the volume instead._ |
| `force` | boolean | False | default | _Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called 'unused[n]', which contains the volume ID. Unlink of unused[n] always cause physical removal._ |
| `freeze` | boolean | False | default | _Freeze CPU at startup (use 'c' monitor command to start execution)._ |
| `hookscript` | string | False | default | _Script that will be executed during various steps in the vms lifetime._ |
| `hostpci_list` | string | False | default | _Map host PCI devices into guest._ |
| `hotplug` | string | False | default | _Selectively enable hotplug features. This is a comma separated list of hotplug features: 'network', 'disk', 'cpu', 'memory' and 'usb'. Use '0' to disable hotplug completely. Value '1' is an alias for the default 'network,disk,usb'._ |
| `hugepages` | string | False | default | _Enable/disable hugepages memory._ |
| `ide_list` | string | False | default | _Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `ipconfig_list` | string | False | default | _cloud-init: Specify IP addresses and gateways for the corresponding interface.  IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.  The special string 'dhcp' can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string 'auto' can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.  If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4. _ |
| `ivshmem` | string | False | default | _Inter-VM shared memory. Useful for direct communication between VMs, or to the host._ |
| `keephugepages` | boolean | False | default | _Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts._ |
| `keyboard` | string | False | default | _Keybord layout for vnc server. Default is read from the '/etc/pve/datacenter.cfg' configuration file.It should not be necessary to set it._ |
| `kvm` | boolean | False | default | _Enable/disable KVM hardware virtualization._ |
| `localtime` | boolean | False | default | _Set the real time clock to local time. This is enabled by default if ostype indicates a Microsoft OS._ |
| `lock` | string | False | default | _Lock/unlock the VM._ |
| `machine` | string | False | default | _Specifies the Qemu machine type._ |
| `memory` | integer | False | default | _Amount of RAM for the VM in MB. This is the maximum available memory when you use the balloon device._ |
| `migrate_downtime` | number | False | default | _Set maximum tolerated downtime (in seconds) for migrations._ |
| `migrate_speed` | integer | False | default | _Set maximum speed (in MB/s) for migrations. Value 0 is no limit._ |
| `name` | string | False | default | _Set a name for the VM. Only used on the configuration web interface._ |
| `nameserver` | string | False | default | _cloud-init: Sets DNS server IP address for a container. Create will'     .' automatically use the setting from the host if neither searchdomain nor nameserver'     .' are set._ |
| `net_list` | string | False | default | _Specify network devices._ |
| `node` | string | True | default | _The cluster node name._ |
| `numa` | boolean | False | default | _Enable/disable NUMA._ |
| `numa_list` | string | False | default | _NUMA topology._ |
| `onboot` | boolean | False | default | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | default | _Specify guest operating system._ |
| `parallel_list` | string | False | default | _Map host parallel devices (n is 0 to 2)._ |
| `protection` | boolean | False | default | _Sets the protection flag of the VM. This will disable the remove VM and remove disk operations._ |
| `reboot` | boolean | False | default | _Allow reboot. If set to '0' the VM exit on reboot._ |
| `revert` | string | False | default | _Revert a pending change._ |
| `rng0` | string | False | default | _Configure a VirtIO-based Random Number Generator._ |
| `sata_list` | string | False | default | _Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsi_list` | string | False | default | _Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsihw` | string | False | default | _SCSI controller model_ |
| `searchdomain` | string | False | default | _cloud-init: Sets DNS search domains for a container. Create will'     .' automatically use the setting from the host if neither searchdomain nor nameserver'     .' are set._ |
| `serial_list` | string | False | default | _Create a serial device inside the VM (n is 0 to 3)_ |
| `shares` | integer | False | default | _Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `smbios1` | string | False | default | _Specify SMBIOS type 1 fields._ |
| `smp` | integer | False | default | _The number of CPUs. Please use option -sockets instead._ |
| `sockets` | integer | False | default | _The number of CPU sockets._ |
| `spice_enhancements` | string | False | default | _Configure additional enhancements for SPICE._ |
| `sshkeys` | string | False | default | _cloud-init: Setup public SSH keys (one key per line, OpenSSH format)._ |
| `startdate` | string | False | default | _Set the initial date of the real time clock. Valid format for date are:'now' or '2006-06-17T16:01:21' or '2006-06-17'._ |
| `startup` | string | False | default | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `tablet` | boolean | False | default | _Enable/disable the USB tablet device._ |
| `tags` | string | False | default | _Tags of the VM. This is only meta information._ |
| `tdf` | boolean | False | default | _Enable/disable time drift fix._ |
| `template` | boolean | False | default | _Enable/disable Template._ |
| `unused_list` | string | False | default | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `usb_list` | string | False | default | _Configure an USB device (n is 0 to 4)._ |
| `vcpus` | integer | False | default | _Number of hotplugged vcpus._ |
| `vga` | string | False | default | _Configure the VGA hardware._ |
| `virtio_list` | string | False | default | _Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `vmgenid` | string | False | default | _Set VM Generation ID. Use '1' to autogenerate on create or update, pass '0' to disable explicitly._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `vmstatestorage` | string | False | default | _Default storage for VM state volumes/files._ |
| `watchdog` | string | False | default | _Create a virtual hardware watchdog device._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `enable` | boolean | False | default | _Enable host firewall rules._ |
| `log_level_in` | string | False | default | _Log level for incoming traffic._ |
| `log_level_out` | string | False | default | _Log level for outgoing traffic._ |
| `log_nf_conntrack` | boolean | False | default | _Enable logging of conntrack information._ |
| `ndp` | boolean | False | default | _Enable NDP (Neighbor Discovery Protocol)._ |
| `nf_conntrack_allow_invalid` | boolean | False | default | _Allow invalid packets on connection tracking._ |
| `nf_conntrack_max` | integer | False | default | _Maximum number of tracked connections._ |
| `nf_conntrack_tcp_timeout_established` | integer | False | default | _Conntrack established timeout._ |
| `nf_conntrack_tcp_timeout_syn_recv` | integer | False | default | _Conntrack syn recv timeout._ |
| `node` | string | True | default | _The cluster node name._ |
| `nosmurfs` | boolean | False | default | _Enable SMURFS filter._ |
| `protection_synflood` | boolean | False | default | _Enable synflood protection_ |
| `protection_synflood_burst` | integer | False | default | _Synflood protection rate burst by ip src._ |
| `protection_synflood_rate` | integer | False | default | _Synflood protection rate syn/sec by ip src._ |
| `smurf_log_level` | string | False | default | _Log level for SMURFS filter._ |
| `tcp_flags_log_level` | string | False | default | _Log level for illegal tcp flags filter._ |
| `tcpflags` | boolean | False | default | _Filter illegal combinations of TCP flags._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_rules_create_rule
_Create new rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | True | default | _Rule type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_ping
_Execute ping._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### pools_index
_Pool index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_pbs_pbsscan
_Scan remote Proxmox Backup Server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `fingerprint` | string | False | default | _Certificate SHA 256 fingerprint._ |
| `node` | string | True | default | _The cluster node name._ |
| `password` | string | True | True | _User password or API token secret._ |
| `port` | integer | False | default | _Optional port._ |
| `server` | string | True | default | _The server address (name or IP)._ |
| `username` | string | True | default | _User-name or API token-ID._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_capabilities_qemu_machines_types
_Get available QEMU/KVM machine types._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_pending_vm_pending
_Get the virtual machine configuration with both current and pending values._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_rules_get_rules
_List rules._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_feature_vm_feature
_Check if feature for virtual machine is available._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `feature` | string | True | default | _Feature to check._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | False | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_file_restore_list
_List files and directories for single file restore under the given path._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `filepath` | string | True | default | _base64-path to the directory or file being listed, or "/"._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `volume` | string | True | default | _Backup volume ID or name. Currently only PBS snapshots are supported._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_sdn_zones_zone_diridx
__

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `zone` | string | True | default | _The SDN zone object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_index
_ACMEAccount index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_custom_remove_custom_cert
_DELETE custom certificate chain and key._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `restart` | boolean | False | default | _Restart pveproxy._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_account_register_account
_Register a new ACME account with CA._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `contact` | string | True | default | _Contact email addresses._ |
| `directory` | string | False | default | _URL of ACME CA directory endpoint._ |
| `name` | string | False | default | _ACME account config file name._ |
| `tos_url` | string | False | default | _URL of CA TermsOfService - setting this indicates agreement._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_zfs_zfsscan
_Scan zfs pool list on local node._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_firewall_rules_pos_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `moveto` | integer | False | default | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | False | default | _Rule type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_zfs_create
_Create a ZFS pool._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | default | _Configure storage using the zpool._ |
| `ashift` | integer | False | default | _Pool sector size exponent._ |
| `compression` | string | False | default | _The compression algorithm to use._ |
| `devices` | string | True | default | _The block devices you want to create the zpool on._ |
| `name` | string | True | default | _The storage identifier._ |
| `node` | string | True | default | _The cluster node name._ |
| `raidlevel` | string | True | default | _The RAID level to use._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_osinfo
_Execute get-osinfo._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_lvm_create
_Create an LVM Volume Group_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | default | _Configure storage using the Volume Group_ |
| `device` | string | True | default | _The block device you want to create the volume group on_ |
| `name` | string | True | default | _The storage identifier._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_ticket_get_ticket
_Dummy. Useful for formatters which want to provide a login page._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_domains_realm_sync
_Syncs users and/or groups from the configured LDAP to user.cfg. NOTE: Synced groups will have the name 'name-$realm', so make sure those groups do not exist to prevent overwriting._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dry_run` | boolean | False | default | _If set, does not write anything._ |
| `enable_new` | boolean | False | default | _Enable newly synced users immediately._ |
| `full` | boolean | False | default | _If set, uses the LDAP Directory as source of truth, deleting users or groups not returned from the sync. Otherwise only syncs information which is not already present, and does not deletes or modifies anything else._ |
| `purge` | boolean | False | default | _Remove ACLs for users or groups which were removed from the config during a sync._ |
| `realm` | string | True | default | _Authentication domain ID_ |
| `scope` | string | False | default | _Select what to sync._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_rrd
_Read VM RRD statistics (returns PNG)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `ds` | string | True | default | _The list of datasources you want to display._ |
| `node` | string | True | default | _The cluster node name._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_spiceproxy
_Returns a SPICE configuration to connect to the VM._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `proxy` | string | False | default | _SPICE proxy server. This can be used by the client to specify the proxy server. All nodes in a cluster runs 'spiceproxy', so it is up to the client to choose one. By default, we return the node where the VM is currently running. As reasonable setting is to use same node you use to connect to the API (This is window.location.hostname for the JS GUI)._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_start_vm_start
_Start virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force_cpu` | string | False | default | _Override QEMU's -cpu argument with the given string._ |
| `machine` | string | False | default | _Specifies the Qemu machine type._ |
| `migratedfrom` | string | False | default | _The cluster node name._ |
| `migration_network` | string | False | default | _CIDR of the (sub) network that is used for migration._ |
| `migration_type` | string | False | default | _Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance._ |
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `stateuri` | string | False | default | _Some command save/restore state from this location._ |
| `targetstorage` | string | False | default | _Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself._ |
| `timeout` | integer | False | default | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_resize_resize_vm
_Extend volume size._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disk` | string | True | default | _The disk you want to resize._ |
| `node` | string | True | default | _The cluster node name._ |
| `size` | string | True | default | _The new size. With the `+` sign the value is added to the actual size of the volume and without it, the value is taken as an absolute one. Shrinking disk size is not supported._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_options_get_options
_Get VM firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hardware_pci_pciscan
_List local PCI devices._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pci_class_blacklist` | string | False | default | _A list of blacklisted PCI classes, which will not be returned. Following are filtered by default: Memory Controller (05), Bridge (06), Generic System Peripheral (08) and Processor (0b)._ |
| `verbose` | boolean | False | default | _If disabled, does only print the PCI IDs. Otherwise, additional information like vendor and device will be returned._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_name_cidr_update_ip
_Update IP or Network settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `nomatch` | boolean | False | default | _Description unavailable._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_sdn_zones_index
_Get status for all zones._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_init
_Create initial ceph default configuration and setup symlinks._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cluster_network` | string | False | default | _Declare a separate cluster network, OSDs will routeheartbeat, object replication and recovery traffic over it_ |
| `disable_cephx` | boolean | False | default | _Disable cephx authentication.  WARNING: cephx is a security feature protecting against man-in-the-middle attacks. Only consider disabling cephx if your network is private!_ |
| `min_size` | integer | False | default | _Minimum number of available replicas per object to allow I/O_ |
| `network` | string | False | default | _Use specific network for all ceph related traffic_ |
| `node` | string | True | default | _The cluster node name._ |
| `pg_bits` | integer | False | default | _Placement group bits, used to specify the default number of placement groups.  NOTE: 'osd pool default pg num' does not work for default pools._ |
| `size` | integer | False | default | _Targeted number of replicas per object_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_index
_Qemu Agent command index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_account_name_get_account
_Return existing ACME account information._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | False | default | _ACME account config file name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmlist
_Virtual machine index (per node)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `full` | boolean | False | default | _Determine the full status of active VMs._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_status_manager_status
_Get full HA manger status, including LRM status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_acme_directories_get_directories
_Get named known ACME directory endpoints._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_restart
_Restart ceph services._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | False | default | _Ceph service name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_migrate_migrate_vm
_Migrate virtual machine. Creates a new migration task._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | integer | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `force` | boolean | False | default | _Allow to migrate VMs which use local devices. Only root may use this option._ |
| `migration_network` | string | False | default | _CIDR of the (sub) network that is used for migration._ |
| `migration_type` | string | False | default | _Migration traffic is encrypted using an SSH tunnel by default. On secure, completely private networks this can be disabled to increase performance._ |
| `node` | string | True | default | _The cluster node name._ |
| `online` | boolean | False | default | _Use online/live migration if VM is running. Ignored if VM is stopped._ |
| `target` | string | True | default | _Target node._ |
| `targetstorage` | string | False | default | _Mapping from source to target storages. Providing only a single storage ID maps all source storages to that storage. Providing the special value '1' will map each source storage to itself._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `with_local_disks` | boolean | False | default | _Enable live storage migration for local disk_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_list_security_groups
_List security groups._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_refs
_Lists possible IPSet/Alias reference which are allowed in source/dest properties._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `prox_type` | string | False | default | _Only list references of specified type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_domains_index
_Authentication domain index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_index
_Cluster index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_unlink
_Unlink/delete disk images._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called 'unused[n]', which contains the volume ID. Unlink of unused[n] always cause physical removal._ |
| `idlist` | string | True | default | _A list of disk IDs you want to delete._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_nodes
_Corosync node list._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_ticket_create_ticket
_Create or verify authentication ticket._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `otp` | string | False | default | _One-time password for Two-factor authentication._ |
| `password` | string | True | True | _The secret password. This can also be a valid ticket._ |
| `path` | string | False | default | _Verify ticket, and check if user have access 'privs' on 'path'_ |
| `privs` | string | False | default | _Verify ticket, and check if user have access 'privs' on 'path'_ |
| `realm` | string | False | default | _You can optionally pass the realm using this parameter. Normally the realm is simply added to the username <username>@<relam>._ |
| `username` | string | True | default | _User name_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_rrd
_Read node RRD statistics (returns PNG)_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `ds` | string | True | default | _The list of datasources you want to display._ |
| `node` | string | True | default | _The cluster node name._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_config_update_vm_async
_Set virtual machine options (asynchrounous API)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `acpi` | boolean | False | default | _Enable/disable ACPI._ |
| `agent` | string | False | default | _Enable/disable Qemu GuestAgent and its properties._ |
| `arch` | string | False | default | _Virtual processor architecture. Defaults to the host._ |
| `args` | string | False | default | _Arbitrary arguments passed to kvm._ |
| `audio0` | string | False | default | _Configure a audio device, useful in combination with QXL/Spice._ |
| `autostart` | boolean | False | default | _Automatic restart after crash (currently ignored)._ |
| `background_delay` | integer | False | default | _Time to wait for the task to finish. We return 'null' if the task finish within that time._ |
| `balloon` | integer | False | default | _Amount of target RAM for the VM in MB. Using zero disables the ballon driver._ |
| `bios` | string | False | default | _Select BIOS implementation._ |
| `boot` | string | False | default | _Specify guest boot order. Use with 'order=', usage with no key or 'legacy=' is deprecated._ |
| `bootdisk` | string | False | default | _Enable booting from specified disk. Deprecated: Use 'boot: order=foo;bar' instead._ |
| `cdrom` | string | False | default | _This is an alias for option -ide2_ |
| `cicustom` | string | False | default | _cloud-init: Specify custom files to replace the automatically generated ones at start._ |
| `cipassword` | string | False | default | _cloud-init: Password to assign the user. Using this is generally not recommended. Use ssh keys instead. Also note that older cloud-init versions do not support hashed passwords._ |
| `citype` | string | False | default | _Specifies the cloud-init configuration format. The default depends on the configured operating system type (`ostype`. We use the `nocloud` format for Linux, and `configdrive2` for windows._ |
| `ciuser` | string | False | default | _cloud-init: User name to change ssh keys and password for instead of the image's configured default user._ |
| `cores` | integer | False | default | _The number of cores per socket._ |
| `cpu` | string | False | default | _Emulated CPU type._ |
| `cpulimit` | number | False | default | _Limit of CPU usage._ |
| `cpuunits` | integer | False | default | _CPU weight for a VM._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `description` | string | False | default | _Description for the VM. Only used on the configuration web interface. This is saved as comment inside the configuration file._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `efidisk0` | string | False | default | _Configure a Disk for storing EFI vars. Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume. Note that SIZE_IN_GiB is ignored here and that the default EFI vars are copied to the volume instead._ |
| `force` | boolean | False | default | _Force physical removal. Without this, we simple remove the disk from the config file and create an additional configuration entry called 'unused[n]', which contains the volume ID. Unlink of unused[n] always cause physical removal._ |
| `freeze` | boolean | False | default | _Freeze CPU at startup (use 'c' monitor command to start execution)._ |
| `hookscript` | string | False | default | _Script that will be executed during various steps in the vms lifetime._ |
| `hostpci_list` | string | False | default | _Map host PCI devices into guest._ |
| `hotplug` | string | False | default | _Selectively enable hotplug features. This is a comma separated list of hotplug features: 'network', 'disk', 'cpu', 'memory' and 'usb'. Use '0' to disable hotplug completely. Value '1' is an alias for the default 'network,disk,usb'._ |
| `hugepages` | string | False | default | _Enable/disable hugepages memory._ |
| `ide_list` | string | False | default | _Use volume as IDE hard disk or CD-ROM (n is 0 to 3). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `ipconfig_list` | string | False | default | _cloud-init: Specify IP addresses and gateways for the corresponding interface.  IP addresses use CIDR notation, gateways are optional but need an IP of the same type specified.  The special string 'dhcp' can be used for IP addresses to use DHCP, in which case no explicit gateway should be provided. For IPv6 the special string 'auto' can be used to use stateless autoconfiguration. This requires cloud-init 19.4 or newer.  If cloud-init is enabled and neither an IPv4 nor an IPv6 address is specified, it defaults to using dhcp on IPv4. _ |
| `ivshmem` | string | False | default | _Inter-VM shared memory. Useful for direct communication between VMs, or to the host._ |
| `keephugepages` | boolean | False | default | _Use together with hugepages. If enabled, hugepages will not not be deleted after VM shutdown and can be used for subsequent starts._ |
| `keyboard` | string | False | default | _Keybord layout for vnc server. Default is read from the '/etc/pve/datacenter.cfg' configuration file.It should not be necessary to set it._ |
| `kvm` | boolean | False | default | _Enable/disable KVM hardware virtualization._ |
| `localtime` | boolean | False | default | _Set the real time clock to local time. This is enabled by default if ostype indicates a Microsoft OS._ |
| `lock` | string | False | default | _Lock/unlock the VM._ |
| `machine` | string | False | default | _Specifies the Qemu machine type._ |
| `memory` | integer | False | default | _Amount of RAM for the VM in MB. This is the maximum available memory when you use the balloon device._ |
| `migrate_downtime` | number | False | default | _Set maximum tolerated downtime (in seconds) for migrations._ |
| `migrate_speed` | integer | False | default | _Set maximum speed (in MB/s) for migrations. Value 0 is no limit._ |
| `name` | string | False | default | _Set a name for the VM. Only used on the configuration web interface._ |
| `nameserver` | string | False | default | _cloud-init: Sets DNS server IP address for a container. Create will'     .' automatically use the setting from the host if neither searchdomain nor nameserver'     .' are set._ |
| `net_list` | string | False | default | _Specify network devices._ |
| `node` | string | True | default | _The cluster node name._ |
| `numa` | boolean | False | default | _Enable/disable NUMA._ |
| `numa_list` | string | False | default | _NUMA topology._ |
| `onboot` | boolean | False | default | _Specifies whether a VM will be started during system bootup._ |
| `ostype` | string | False | default | _Specify guest operating system._ |
| `parallel_list` | string | False | default | _Map host parallel devices (n is 0 to 2)._ |
| `protection` | boolean | False | default | _Sets the protection flag of the VM. This will disable the remove VM and remove disk operations._ |
| `reboot` | boolean | False | default | _Allow reboot. If set to '0' the VM exit on reboot._ |
| `revert` | string | False | default | _Revert a pending change._ |
| `rng0` | string | False | default | _Configure a VirtIO-based Random Number Generator._ |
| `sata_list` | string | False | default | _Use volume as SATA hard disk or CD-ROM (n is 0 to 5). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsi_list` | string | False | default | _Use volume as SCSI hard disk or CD-ROM (n is 0 to 30). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `scsihw` | string | False | default | _SCSI controller model_ |
| `searchdomain` | string | False | default | _cloud-init: Sets DNS search domains for a container. Create will'     .' automatically use the setting from the host if neither searchdomain nor nameserver'     .' are set._ |
| `serial_list` | string | False | default | _Create a serial device inside the VM (n is 0 to 3)_ |
| `shares` | integer | False | default | _Amount of memory shares for auto-ballooning. The larger the number is, the more memory this VM gets. Number is relative to weights of all other running VMs. Using zero disables auto-ballooning. Auto-ballooning is done by pvestatd._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `smbios1` | string | False | default | _Specify SMBIOS type 1 fields._ |
| `smp` | integer | False | default | _The number of CPUs. Please use option -sockets instead._ |
| `sockets` | integer | False | default | _The number of CPU sockets._ |
| `spice_enhancements` | string | False | default | _Configure additional enhancements for SPICE._ |
| `sshkeys` | string | False | default | _cloud-init: Setup public SSH keys (one key per line, OpenSSH format)._ |
| `startdate` | string | False | default | _Set the initial date of the real time clock. Valid format for date are:'now' or '2006-06-17T16:01:21' or '2006-06-17'._ |
| `startup` | string | False | default | _Startup and shutdown behavior. Order is a non-negative number defining the general startup order. Shutdown in done with reverse ordering. Additionally you can set the 'up' or 'down' delay in seconds, which specifies a delay to wait before the next VM is started or stopped._ |
| `tablet` | boolean | False | default | _Enable/disable the USB tablet device._ |
| `tags` | string | False | default | _Tags of the VM. This is only meta information._ |
| `tdf` | boolean | False | default | _Enable/disable time drift fix._ |
| `template` | boolean | False | default | _Enable/disable Template._ |
| `unused_list` | string | False | default | _Reference to unused volumes. This is used internally, and should not be modified manually._ |
| `usb_list` | string | False | default | _Configure an USB device (n is 0 to 4)._ |
| `vcpus` | integer | False | default | _Number of hotplugged vcpus._ |
| `vga` | string | False | default | _Configure the VGA hardware._ |
| `virtio_list` | string | False | default | _Use volume as VIRTIO hard disk (n is 0 to 15). Use the special syntax STORAGE_ID:SIZE_IN_GiB to allocate a new volume._ |
| `vmgenid` | string | False | default | _Set VM Generation ID. Use '1' to autogenerate on create or update, pass '0' to disable explicitly._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `vmstatestorage` | string | False | default | _Default storage for VM state volumes/files._ |
| `watchdog` | string | False | default | _Create a virtual hardware watchdog device._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_fstrim
_Execute fstrim._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_rules_pos_update_rule
_Modify rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | False | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `moveto` | integer | False | default | _Move rule to new position <moveto>. Other arguments are ignored._ |
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | False | default | _Rule type._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_ipams_ipam_delete
_Delete sdn ipam object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `ipam` | string | True | default | _The SDN ipam object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_replication_id_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backup_id_included_volumes_get_volume_backup_included
_Returns included guests and the backup status of their disks. Optimized to be used in ExtJS tree views._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _The job ID._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_shutdown
_Execute shutdown._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backupinfo_not_backed_up_get_guests_not_in_backup
_Shows all guests which are not covered by any backup job._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot
_Snapshot a container._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `description` | string | False | default | _A textual description or comment._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_groups_groupid_read_group
_Get group configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `groupid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_template
_Create a Template._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_name_create_ip
_Add IP or Network to IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `name` | string | True | default | _IP set name._ |
| `nomatch` | boolean | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_rules_create_rule
_Create new rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `action` | string | True | default | _Rule action ('ACCEPT', 'DROP', 'REJECT') or security group name._ |
| `comment` | string | False | default | _Descriptive comment._ |
| `dest` | string | False | default | _Restrict packet destination address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dport` | string | False | default | _Restrict TCP/UDP destination port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `enable` | integer | False | default | _Flag to enable/disable a rule._ |
| `icmp_type` | string | False | default | _Specify icmp-type. Only valid if proto equals 'icmp'._ |
| `iface` | string | False | default | _Network interface name. You have to use network configuration key names for VMs and containers ('net\d+'). Host related rules can use arbitrary strings._ |
| `log` | string | False | default | _Log level for firewall rule._ |
| `macro` | string | False | default | _Use predefined standard macro._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `proto` | string | False | default | _IP protocol. You can use protocol names ('tcp'/'udp') or simple numbers, as defined in '/etc/protocols'._ |
| `source` | string | False | default | _Restrict packet source address. This can refer to a single IP address, an IP set ('+ipsetname') or an IP alias definition. You can also specify an address range like '20.34.101.207-201.3.9.99', or a list of IP addresses and networks (entries are separated by comma). Please do not mix IPv4 and IPv6 addresses inside such lists._ |
| `sport` | string | False | default | _Restrict TCP/UDP source port. You can use service names or simple numbers (0-65535), as defined in '/etc/services'. Port ranges can be specified with '\d+:\d+', for example '80:85', and you can use comma separated list to match several ports or ranges._ |
| `prox_type` | string | True | default | _Rule type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_ipset_index
_List IPSets_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_index
_Directory index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_lvmthin_lvmthinscan
_List local LVM Thin Pools._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vg` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_status_current_status
_Get HA manger status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_netstat
_Read tap/vm network device interface counters_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_rules_pos_get_rule
_Get single rule data._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_wakeonlan
_Try to wake a node via 'wake on LAN' network packet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _target node for wake on LAN packet_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_options_get_options
_Get datacenter options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_users_create_user
_Create new user._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description unavailable._ |
| `email` | string | False | default | _Description unavailable._ |
| `enable` | boolean | False | default | _Enable the account (default). You can set this to '0' to disable the account_ |
| `expire` | integer | False | default | _Account expiration date (seconds since epoch). '0' means no expiration date._ |
| `firstname` | string | False | default | _Description unavailable._ |
| `groups` | string | False | default | _Description unavailable._ |
| `keys` | string | False | default | _Keys for two factor auth (yubico)._ |
| `lastname` | string | False | default | _Description unavailable._ |
| `password` | string | False | True | _Initial password._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_time
_Read server time and time zone settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### storage_create
_Create a new storage._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `authsupported` | string | False | default | _Authsupported._ |
| `base` | string | False | default | _Base volume. This volume is automatically activated._ |
| `blocksize` | string | False | default | _block size_ |
| `bwlimit` | string | False | default | _Set bandwidth/io limits various operations._ |
| `comstar_hg` | string | False | default | _host group for comstar views_ |
| `comstar_tg` | string | False | default | _target group for comstar views_ |
| `content` | string | False | default | _Allowed content types.  NOTE: the value 'rootdir' is used for Containers, and value 'images' for VMs. _ |
| `datastore` | string | False | default | _Proxmox Backup Server datastore name._ |
| `disable` | boolean | False | default | _Flag to disable the storage._ |
| `domain` | string | False | default | _CIFS domain._ |
| `encryption_key` | string | False | default | _Encryption key. Use 'autogen' to generate one automatically without passphrase._ |
| `export` | string | False | default | _NFS export path._ |
| `fingerprint` | string | False | default | _Certificate SHA 256 fingerprint._ |
| `prox_format` | string | False | default | _Default image format._ |
| `fuse` | boolean | False | default | _Mount CephFS through FUSE._ |
| `is_mountpoint` | string | False | default | _Assume the given path is an externally managed mountpoint and consider the storage offline if it is not mounted. Using a boolean (yes/no) value serves as a shortcut to using the target path in this field._ |
| `iscsiprovider` | string | False | default | _iscsi provider_ |
| `krbd` | boolean | False | default | _Always access rbd through krbd kernel module._ |
| `lio_tpg` | string | False | default | _target portal group for Linux LIO targets_ |
| `master_pubkey` | string | False | default | _Base64-encoded, PEM-formatted public RSA key. Used tp encrypt a copy of the encryption-key which will be added to each encrypted backup._ |
| `maxfiles` | integer | False | default | _Maximal number of backup files per VM. Use '0' for unlimted._ |
| `mkdir` | boolean | False | default | _Create the directory if it doesn't exist._ |
| `monhost` | string | False | default | _IP addresses of monitors (for external clusters)._ |
| `mountpoint` | string | False | default | _mount point_ |
| `namespace` | string | False | default | _RBD Namespace._ |
| `nodes` | string | False | default | _List of cluster node names._ |
| `nowritecache` | boolean | False | default | _disable write caching on the target_ |
| `options` | string | False | default | _NFS mount options (see 'man nfs')_ |
| `password` | string | False | True | _Password for accessing the share/datastore._ |
| `path` | string | False | default | _File system path._ |
| `pool` | string | False | default | _Pool._ |
| `port` | integer | False | default | _For non default port._ |
| `portal` | string | False | default | _iSCSI portal (IP or DNS name with optional port)._ |
| `prune_backups` | string | False | default | _The retention options with shorter intervals are processed first with --keep-last being the very first one. Each option covers a specific period of time. We say that backups within this period are covered by this option. The next option does not take care of already covered backups and only considers older backups._ |
| `redundancy` | integer | False | default | _The redundancy count specifies the number of nodes to which the resource should be deployed. It must be at least 1 and at most the number of nodes in the cluster._ |
| `saferemove` | boolean | False | default | _Zero-out data when removing LVs._ |
| `saferemove_throughput` | string | False | default | _Wipe throughput (cstream -t parameter value)._ |
| `server` | string | False | default | _Server IP or DNS name._ |
| `server2` | string | False | default | _Backup volfile server IP or DNS name._ |
| `share` | string | False | default | _CIFS share._ |
| `shared` | boolean | False | default | _Mark storage as shared._ |
| `smbversion` | string | False | default | _SMB protocol version_ |
| `sparse` | boolean | False | default | _use sparse volumes_ |
| `storage` | string | True | default | _The storage identifier._ |
| `subdir` | string | False | default | _Subdir to mount._ |
| `tagged_only` | boolean | False | default | _Only use logical volumes tagged with 'pve-vm-ID'._ |
| `target` | string | False | default | _iSCSI target._ |
| `thinpool` | string | False | default | _LVM thin pool LV name._ |
| `transport` | string | False | default | _Gluster transport: tcp or rdma_ |
| `prox_type` | string | True | default | _Storage type._ |
| `username` | string | False | default | _RBD Id._ |
| `vgname` | string | False | default | _Volume group name._ |
| `volume` | string | False | default | _Glusterfs Volume._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_vcpus
_Execute get-vcpus._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_stop_vm_stop
_Stop virtual machine. The qemu process will exit immediately. Thisis akin to pulling the power plug of a running computer and may damage the VM data_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `keepActive` | boolean | False | default | _Do not deactivate storage volumes._ |
| `migratedfrom` | string | False | default | _The cluster node name._ |
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `timeout` | integer | False | default | _Wait maximal timeout seconds._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_index
_Index of available scan methods_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_ipams_ipam_update
_Update sdn ipam object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `ipam` | string | True | default | _The SDN ipam object identifier._ |
| `section` | integer | False | default | _Description unavailable._ |
| `token` | string | False | default | _Description unavailable._ |
| `url` | string | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_roles_roleid_delete_role
_Delete role._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `roleid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_host_name
_Execute get-host-name._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_move_volume
_Move a rootfs-/mp-volume to a different storage_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | number | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `delete` | boolean | False | default | _Delete the original volume after successful copy. By default the original is kept as an unused volume entry._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _Target Storage._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `volume` | string | True | default | _Volume which will be moved._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_report
_Gather various systems information about a node_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_groups_group_pos_delete_rule
_Delete rule._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `group` | string | True | default | _Security Group name._ |
| `pos` | integer | False | default | _Update rule at position <pos>._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_options_set_options
_Set Firewall options._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `dhcp` | boolean | False | default | _Enable DHCP._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `enable` | boolean | False | default | _Enable/disable firewall rules._ |
| `ipfilter` | boolean | False | default | _Enable default IP filters. This is equivalent to adding an empty ipfilter-net<id> ipset for every interface. Such ipsets implicitly contain sane default restrictions such as restricting IPv6 link local addresses to the one derived from the interface's MAC address. For containers the configured IP addresses will be implicitly added._ |
| `log_level_in` | string | False | default | _Log level for incoming traffic._ |
| `log_level_out` | string | False | default | _Log level for outgoing traffic._ |
| `macfilter` | boolean | False | default | _Enable/disable MAC address filter._ |
| `ndp` | boolean | False | default | _Enable NDP (Neighbor Discovery Protocol)._ |
| `node` | string | True | default | _The cluster node name._ |
| `policy_in` | string | False | default | _Input policy._ |
| `policy_out` | string | False | default | _Output policy._ |
| `radv` | boolean | False | default | _Allow sending Router Advertisement._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_lvmthin_index
_List LVM thinpools_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_vncshell
_Creates a VNC Shell proxy._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cmd` | string | False | default | _Run specific command or default to login._ |
| `cmd_opts` | string | False | default | _Add parameters to a command. Encoded as null terminated strings._ |
| `height` | integer | False | default | _sets the height of the console in pixels._ |
| `node` | string | True | default | _The cluster node name._ |
| `upgrade` | boolean | False | default | _Deprecated, use the 'cmd' property instead! Run 'apt-get dist-upgrade' instead of normal shell._ |
| `websocket` | boolean | False | default | _use websocket instead of standard vnc._ |
| `width` | integer | False | default | _sets the width of the console in pixels._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot_snapname_rollback
_Rollback LXC state to specified snapshot._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_replication_id_log_read_job_log
_Read replication job log._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_id` | string | True | default | _Replication Job ID. The ID is composed of a Guest ID and a job number, separated by a hyphen, i.e. '<GUEST>-<JOBNUM>'._ |
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `start` | integer | False | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_vnets_vnet_subnets_create
_Create a new sdn subnet object._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dnszoneprefix` | string | False | default | _dns domain zone prefix  ex: 'adm' -> <hostname>.adm.mydomain.com_ |
| `gateway` | string | False | default | _Subnet Gateway: Will be assign on vnet for layer3 zones_ |
| `snat` | boolean | False | default | _enable masquerade for this subnet if pve-firewall_ |
| `subnet` | string | True | default | _The SDN subnet object identifier._ |
| `prox_type` | string | True | default | _Description unavailable._ |
| `vnet` | string | True | default | _associated vnet_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_disks_smart
_Get SMART Health of a disk._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `disk` | string | True | default | _Block device name_ |
| `healthonly` | boolean | False | default | _If true returns only the health status_ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_config_nodes_node_addnode
_Adds a node to the cluster configuration. This call is for internal use._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `apiversion` | integer | False | default | _The JOIN_API_VERSION of the new node._ |
| `force` | boolean | False | default | _Do not throw error if node already exists._ |
| `link_list` | string | False | default | _Address and priority information of a single corosync link. (up to 8 links supported; link0..link7)_ |
| `new_node_ip` | string | False | default | _IP Address of node to add. Used as fallback if no links are given._ |
| `node` | string | True | default | _The cluster node name._ |
| `nodeid` | integer | False | default | _Node id for this node._ |
| `votes` | integer | False | default | _Number of votes for this node_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_dns_update_dns
_Write DNS settings._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns1` | string | False | default | _First name server IP address._ |
| `dns2` | string | False | default | _Second name server IP address._ |
| `dns3` | string | False | default | _Third name server IP address._ |
| `node` | string | True | default | _The cluster node name._ |
| `search` | string | True | default | _Search domain for host-name lookup._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### pools_poolid_read_pool
_Get pool configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `poolid` | string | True | default | _Description unavailable._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_fsfreeze_thaw
_Execute fsfreeze-thaw._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_name_create_ip
_Add IP or Network to IPSet._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `nomatch` | boolean | False | default | _Description unavailable._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_index
_List HA resources._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_type` | string | False | default | _Only list resources of specific type_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_snapshot_snapname_config_update_snapshot_config
_Update snapshot metadata._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `description` | string | False | default | _A textual description or comment._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_syslog
_Read system log_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `limit` | integer | False | default | _Description unavailable._ |
| `node` | string | True | default | _The cluster node name._ |
| `service` | string | False | default | _Service ID_ |
| `since` | string | False | default | _Display all log since this date-time string._ |
| `start` | integer | False | default | _Description unavailable._ |
| `until` | string | False | default | _Display all log until this date-time string._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_destroy_vm
_Destroy the container (also delete all uses files)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `destroy_unreferenced_disks` | boolean | False | default | _If set, destroy additionally all disks with the VMID from all enabled storages which are not referenced in the config._ |
| `force` | boolean | False | default | _Force destroy, even if running._ |
| `node` | string | True | default | _The cluster node name._ |
| `purge` | boolean | False | default | _Remove container from all related configurations. For example, backup jobs, replication jobs or HA. Related ACLs and Firewall entries will *always* be removed._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_ipset_ipset_index
_List IPSets_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_configdb
_Get Ceph configuration database._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_snapshot_snapname_delsnapshot
_Delete a LXC snapshot._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `force` | boolean | False | default | _For removal from config file, even if removing disk snapshots fails._ |
| `node` | string | True | default | _The cluster node name._ |
| `snapname` | string | True | default | _The name of the snapshot._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_sid_update
_Update resource configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description._ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `group` | string | False | default | _The HA group identifier._ |
| `max_relocate` | integer | False | default | _Maximal number of service relocate tries when a service failes to start._ |
| `max_restart` | integer | False | default | _Maximal number of tries to restart the service on a node after its start failed._ |
| `sid` | string | True | default | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
| `state` | string | False | default | _Requested resource state._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_termproxy
_Creates a TCP proxy connection._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_osd_osdid_destroyosd
_Destroy OSD_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cleanup` | boolean | False | default | _If set, we remove partition table entries._ |
| `node` | string | True | default | _The cluster node name._ |
| `osdid` | integer | True | default | _OSD ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_move_disk_move_vm_disk
_Move volume to different storage._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | integer | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `delete` | boolean | False | default | _Delete the original disk after successful copy. By default the original disk is kept as unused disk._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `disk` | string | True | default | _The disk you want to move._ |
| `prox_format` | string | False | default | _Target Format._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _Target storage._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_firewall_ipset_name_delete_ipset
_Delete IPSet_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `name` | string | True | default | _IP set name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ceph_status
_Get ceph status._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_tasks
_Read task list for one node (finished tasks)._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `errors` | boolean | False | default | _Description unavailable._ |
| `limit` | integer | False | default | _Only list this amount of tasks._ |
| `node` | string | True | default | _The cluster node name._ |
| `source` | string | False | default | _List archived, active or all tasks._ |
| `start` | integer | False | default | _List tasks beginning from this offset._ |
| `typefilter` | string | False | default | _Only list tasks of this type (e.g., vzstart, vzdump)._ |
| `userfilter` | string | False | default | _Only list tasks from this user._ |
| `vmid` | integer | False | default | _Only list tasks for this VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_sendkey_vm_sendkey
_Send key event to virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `key` | string | True | True | _The key (qemu monitor encoding)._ |
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_certificates_acme_index
_ACME index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_rrddata
_Read node RRD statistics_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cf` | string | False | default | _The RRD consolidation function_ |
| `node` | string | True | default | _The cluster node name._ |
| `timeframe` | string | True | default | _Specify the time frame you are interested in._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_index
_Node index._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_password_change_password
_Change user password._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `password` | string | True | True | _The new password._ |
| `userid` | string | True | default | _User ID_ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_hardware_pci_pciid_mdev_mdevscan
_List mediated device types for given PCI device._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `pciid` | string | True | default | _The PCI ID to list the mdev types for._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_migrate_migrate_vm_precondition
_Get preconditions for migration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `target` | string | False | default | _Target node._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_replication_index
_List replication jobs._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_controllers_create
_Create a new sdn controller object._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `asn` | integer | False | default | _autonomous system number_ |
| `controller` | string | True | default | _The SDN controller object identifier._ |
| `ebgp` | boolean | False | default | _Enable ebgp. (remote-as external)_ |
| `ebgp_multihop` | integer | False | default | _Description unavailable._ |
| `loopback` | string | False | default | _source loopback interface._ |
| `node` | string | False | default | _The cluster node name._ |
| `peers` | string | False | default | _peers address list._ |
| `prox_type` | string | True | default | _Plugin type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_ceph_fs_name_createfs
_Create a Ceph filesystem_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `add_storage` | boolean | False | default | _Configure the created CephFS as storage for this cluster._ |
| `name` | string | False | default | _The ceph filesystem name._ |
| `node` | string | True | default | _The cluster node name._ |
| `pg_num` | integer | False | default | _Number of placement groups for the backing data pool. The metadata pool will use a quarter of this._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_suspend_ram
_Execute suspend-ram._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_vmdiridx
_Directory index_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_agent_get_time
_Execute get-time._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_lxc_vmid_firewall_ipset_name_cidr_update_ip
_Update IP or Network settings_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `cidr` | string | True | default | _Network/IP specification in CIDR format._ |
| `comment` | string | False | default | _Description unavailable._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _IP set name._ |
| `node` | string | True | default | _The cluster node name._ |
| `nomatch` | boolean | False | default | _Description unavailable._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_status_reset_vm_reset
_Reset virtual machine._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `skiplock` | boolean | False | default | _Ignore locks - only root is allowed to use this option._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_zones_zone_update
_Update sdn zone object configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bridge` | string | False | default | _Description unavailable._ |
| `controller` | string | False | default | _Frr router name_ |
| `delete` | string | False | default | _A list of settings you want to delete._ |
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `dns` | string | False | default | _dns api server_ |
| `dnszone` | string | False | default | _dns domain zone  ex: mydomain.com_ |
| `dp_id` | integer | False | default | _Faucet dataplane id_ |
| `exitnodes` | string | False | default | _List of cluster node names._ |
| `ipam` | string | False | default | _use a specific ipam_ |
| `mac` | string | False | default | _Anycast logical router mac address_ |
| `mtu` | integer | False | default | _MTU_ |
| `nodes` | string | False | default | _List of cluster node names._ |
| `peers` | string | False | default | _peers address list._ |
| `reversedns` | string | False | default | _reverse dns api server_ |
| `tag` | integer | False | default | _Service-VLAN Tag_ |
| `vlan_protocol` | string | False | default | _Description unavailable._ |
| `vrf_vxlan` | integer | False | default | _l3vni._ |
| `zone` | string | True | default | _The SDN zone object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### access_tfa_verify_tfa
_Finish a u2f challenge._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `response` | string | True | default | _The response to the current authentication challenge._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_network_create_network
_Create network device configuration_

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `address` | string | False | default | _IP address._ |
| `address6` | string | False | default | _IP address._ |
| `autostart` | boolean | False | default | _Automatically start interface on boot._ |
| `bond_primary` | string | False | default | _Specify the primary interface for active-backup bond._ |
| `bond_mode` | string | False | default | _Bonding mode._ |
| `bond_xmit_hash_policy` | string | False | default | _Selects the transmit hash policy to use for slave selection in balance-xor and 802.3ad modes._ |
| `bridge_ports` | string | False | default | _Specify the interfaces you want to add to your bridge._ |
| `bridge_vlan_aware` | boolean | False | default | _Enable bridge vlan support._ |
| `cidr` | string | False | default | _IPv4 CIDR._ |
| `cidr6` | string | False | default | _IPv6 CIDR._ |
| `comments` | string | False | default | _Comments_ |
| `comments6` | string | False | default | _Comments_ |
| `gateway` | string | False | default | _Default gateway address._ |
| `gateway6` | string | False | default | _Default ipv6 gateway address._ |
| `iface` | string | True | default | _Network interface name._ |
| `mtu` | integer | False | default | _MTU._ |
| `netmask` | string | False | default | _Network mask._ |
| `netmask6` | integer | False | default | _Network mask._ |
| `node` | string | True | default | _The cluster node name._ |
| `ovs_bonds` | string | False | default | _Specify the interfaces used by the bonding device._ |
| `ovs_bridge` | string | False | default | _The OVS bridge associated with a OVS port. This is required when you create an OVS port._ |
| `ovs_options` | string | False | default | _OVS interface options._ |
| `ovs_ports` | string | False | default | _Specify the interfaces you want to add to your bridge._ |
| `ovs_tag` | integer | False | default | _Specify a VLan tag (used by OVSPort, OVSIntPort, OVSBond)_ |
| `slaves` | string | False | default | _Specify the interfaces used by the bonding device._ |
| `prox_type` | string | True | default | _Network interface type_ |
| `vlan_id` | integer | False | default | _vlan-id for a custom named vlan interface (ifupdown2 only)._ |
| `vlan_raw_device` | string | False | default | _Specify the raw interface for the vlan interface._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_backup_create_job
_Create new vzdump backup job._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `prox_all` | boolean | False | default | _Backup all known guest systems on this host._ |
| `bwlimit` | integer | False | default | _Limit I/O bandwidth (KBytes per second)._ |
| `compress` | string | False | default | _Compress dump file._ |
| `dow` | string | False | default | _Day of week selection._ |
| `dumpdir` | string | False | default | _Store resulting files to specified directory._ |
| `enabled` | boolean | False | default | _Enable or disable the job._ |
| `exclude` | string | False | default | _Exclude specified guest systems (assumes --all)_ |
| `exclude_path` | string | False | default | _Exclude certain files/directories (shell globs). Paths starting with '/' are anchored to the container's root,  other paths match relative to each subdirectory._ |
| `ionice` | integer | False | default | _Set CFQ ionice priority._ |
| `lockwait` | integer | False | default | _Maximal time to wait for the global lock (minutes)._ |
| `mailnotification` | string | False | default | _Specify when to send an email_ |
| `mailto` | string | False | default | _Comma-separated list of email addresses or users that should receive email notifications._ |
| `maxfiles` | integer | False | default | _Maximal number of backup files per guest system._ |
| `mode` | string | False | default | _Backup mode._ |
| `node` | string | False | default | _Only run if executed on this node._ |
| `pigz` | integer | False | default | _Use pigz instead of gzip when N>0. N=1 uses half of cores, N>1 uses N as thread count._ |
| `pool` | string | False | default | _Backup all known guest systems included in the specified pool._ |
| `prune_backups` | string | False | default | _Use these retention options instead of those from the storage configuration._ |
| `quiet` | boolean | False | default | _Be quiet._ |
| `remove` | boolean | False | default | _Remove old backup files if there are more than 'maxfiles' backup files._ |
| `script` | string | False | default | _Use specified hook script._ |
| `size` | integer | False | default | _Unused, will be removed in a future release._ |
| `starttime` | string | True | default | _Job Start time._ |
| `stdexcludes` | boolean | False | default | _Exclude temporary files and logs._ |
| `stop` | boolean | False | default | _Stop running backup jobs on this host._ |
| `stopwait` | integer | False | default | _Maximal time to wait until a guest system is stopped (minutes)._ |
| `storage` | string | False | default | _Store resulting file to this storage._ |
| `tmpdir` | string | False | default | _Store temporary files to specified directory._ |
| `vmid` | string | False | default | _The ID of the guest system you want to backup._ |
| `zstd` | integer | False | default | _Zstd threads. N=0 uses half of the available cores, N>0 uses N as thread count._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_scan_glusterfs_glusterfsscan
_Scan remote GlusterFS server._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `node` | string | True | default | _The cluster node name._ |
| `server` | string | True | default | _The server address (name or IP)._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_ha_resources_create
_Create a new HA resource._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `comment` | string | False | default | _Description._ |
| `group` | string | False | default | _The HA group identifier._ |
| `max_relocate` | integer | False | default | _Maximal number of service relocate tries when a service failes to start._ |
| `max_restart` | integer | False | default | _Maximal number of tries to restart the service on a node after its start failed._ |
| `sid` | string | True | default | _HA resource ID. This consists of a resource type followed by a resource specific name, separated with colon (example: vm:100 / ct:100). For virtual machines and containers, you can simply use the VM or CT id as a shortcut (example: 100)._ |
| `state` | string | False | default | _Requested resource state._ |
| `prox_type` | string | False | default | _Resource type._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_execute
_Execute multiple commands in order._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `commands` | string | True | default | _JSON encoded array of commands._ |
| `node` | string | True | default | _The cluster node name._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### storage_storage_delete
_Delete storage configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `storage` | string | True | default | _The storage identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### cluster_sdn_dns_dns_read
_Read sdn dns configuration._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `dns` | string | True | default | _The SDN dns object identifier._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_firewall_aliases_name_remove_alias
_Remove IP or Network alias._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `digest` | string | False | default | _Prevent changes if current configuration file has different SHA1 digest. This can be used to prevent concurrent modifications._ |
| `name` | string | True | default | _Alias name._ |
| `node` | string | True | default | _The cluster node name._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_qemu_vmid_clone_clone_vm
_Create a copy of virtual machine/template._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `bwlimit` | integer | False | default | _Override I/O bandwidth limit (in KiB/s)._ |
| `description` | string | False | default | _Description for the new VM._ |
| `prox_format` | string | False | default | _Target format for file storage. Only valid for full clone._ |
| `full` | boolean | False | default | _Create a full copy of all disks. This is always done when you clone a normal VM. For VM templates, we try to create a linked clone by default._ |
| `name` | string | False | default | _Set a name for the new VM._ |
| `newid` | integer | True | default | _VMID for the clone._ |
| `node` | string | True | default | _The cluster node name._ |
| `pool` | string | False | default | _Add the new VM to the specified pool._ |
| `snapname` | string | False | default | _The name of the snapshot._ |
| `storage` | string | False | default | _Target storage for full clone._ |
| `target` | string | False | default | _Target node. Only allowed if the original VM is on shared storage._ |
| `vmid` | integer | True | default | _The (unique) ID of the VM._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |
### nodes_node_storage_storage_file_restore_download
_Extract a file or directory (as zip archive) from a PBS backup._

| Parameter | Type | Required | Secret | Description |
|---|---|---|---|---|
| `filepath` | string | True | default | _base64-path to the directory or file to download._ |
| `node` | string | True | default | _The cluster node name._ |
| `storage` | string | True | default | _The storage identifier._ |
| `volume` | string | True | default | _Backup volume ID or name. Currently only PBS snapshots are supported._ |
| `profile_name` | string | False | default | _The profile to use to run the action._ |



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