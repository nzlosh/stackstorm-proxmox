import json
from packlib.base import ProxmoxAction


class NodesNodeStorageStorageDownloadUrlDownloadUrlAction(ProxmoxAction):
    """
    Download templates and ISO images by using an URL.
    """

    def run(self, content, filename, node, storage, url, checksum=None, checksum_algorithm=None, verify_certificates=True, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["checksum", checksum, "string"],
            ["checksum-algorithm", checksum_algorithm, "string"],
            ["content", content, "string"],
            ["filename", filename, "string"],
            ["node", node, "string"],
            ["storage", storage, "string"],
            ["url", url, "string"],
            ["verify-certificates", verify_certificates, "boolean"],
            
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
            f"nodes/{node}/storage/{storage}/download-url",
            **proxmox_kwargs
        )
        