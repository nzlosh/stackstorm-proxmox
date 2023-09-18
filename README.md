# proxmox pack

> Enable StackStorm to interact with the Proxmox APIv2.

## Action Generation

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


There are no actions available for this pack.


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