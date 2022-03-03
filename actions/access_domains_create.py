import json
from packlib.base import ProxmoxAction


class AccessDomainsCreateAction(ProxmoxAction):
    """
    Add an authentication server.
    """

    def run(
        self,
        realm,
        prox_type,
        autocreate=False,
        base_dn=None,
        bind_dn=None,
        capath="/etc/ssl/certs",
        case_sensitive=True,
        cert=None,
        certkey=None,
        client_id=None,
        client_key=None,
        comment=None,
        default=None,
        domain=None,
        prox_filter=None,
        group_classes="groupOfNames, group, univentionGroup, ipausergroup",
        group_dn=None,
        group_filter=None,
        group_name_attr=None,
        issuer_url=None,
        mode="ldap",
        password=None,
        port=None,
        secure=None,
        server1=None,
        server2=None,
        sslversion=None,
        sync_defaults_options=None,
        sync_attributes=None,
        tfa=None,
        user_attr=None,
        user_classes="inetorgperson, posixaccount, person, user",
        username_claim=None,
        verify=False,
        profile_name=None,
    ):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["autocreate", autocreate, "boolean"],
            ["base_dn", base_dn, "string"],
            ["bind_dn", bind_dn, "string"],
            ["capath", capath, "string"],
            ["case-sensitive", case_sensitive, "boolean"],
            ["cert", cert, "string"],
            ["certkey", certkey, "string"],
            ["client-id", client_id, "string"],
            ["client-key", client_key, "string"],
            ["comment", comment, "string"],
            ["default", default, "boolean"],
            ["domain", domain, "string"],
            ["filter", prox_filter, "string"],
            ["group_classes", group_classes, "string"],
            ["group_dn", group_dn, "string"],
            ["group_filter", group_filter, "string"],
            ["group_name_attr", group_name_attr, "string"],
            ["issuer-url", issuer_url, "string"],
            ["mode", mode, "string"],
            ["password", password, "string"],
            ["port", port, "integer"],
            ["realm", realm, "string"],
            ["secure", secure, "boolean"],
            ["server1", server1, "string"],
            ["server2", server2, "string"],
            ["sslversion", sslversion, "string"],
            ["sync-defaults-options", sync_defaults_options, "string"],
            ["sync_attributes", sync_attributes, "string"],
            ["tfa", tfa, "string"],
            ["type", prox_type, "string"],
            ["user_attr", user_attr, "string"],
            ["user_classes", user_classes, "string"],
            ["username-claim", username_claim, "string"],
            ["verify", verify, "boolean"],
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

        return self.proxmox.post(f"access/domains", **proxmox_kwargs)
