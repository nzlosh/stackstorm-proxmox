import json
from packlib.base import ProxmoxAction


class AccessDomainsCreateAction(ProxmoxAction):
    """
    Add an authentication server.
    """

    def run(self, realm, prox_type, base_dn=None, bind_dn=None, capath=None, cert=None, certkey=None, comment=None, default=None, domain=None, port=None, secure=None, server1=None, server2=None, sslversion=None, tfa=None, user_attr=None, verify=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["base_dn", base_dn, "string"],
            ["bind_dn", bind_dn, "string"],
            ["capath", capath, "string"],
            ["cert", cert, "string"],
            ["certkey", certkey, "string"],
            ["comment", comment, "string"],
            ["default", default, "boolean"],
            ["domain", domain, "string"],
            ["port", port, "integer"],
            ["realm", realm, "string"],
            ["secure", secure, "boolean"],
            ["server1", server1, "string"],
            ["server2", server2, "string"],
            ["sslversion", sslversion, "string"],
            ["tfa", tfa, "string"],
            ["type", prox_type, "string"],
            ["user_attr", user_attr, "string"],
            ["verify", verify, "boolean"],
            
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
            f"access/domains",
            **proxmox_kwargs
        )
        