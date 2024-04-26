# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action
from proxmoxer import ProxmoxAPI

LOG = logging.getLogger(__name__)


class ProxmoxAction(Action):
    def __init__(self, config):
        super().__init__(config)
        self.config = config

    def run(self, profile_name=None, api_timeout=5):
        super().run()

        if not profile_name:
            profile_name = self.config.get("default_profile")
            if not profile_name:
                raise ValueError(f"No profile in pack configuration or supplied in action.")

        for profile in self.config.get("profiles", {}):
            if profile["name"] == profile_name:
                break
        else:
            raise ValueError(f"Profile '{profile_name}' can't be found in pack configuration.")

        self.proxmox = ProxmoxAPI(
            profile.get("host"),
            user=profile.get("username") + "@" + profile.get("auth_realm"),
            password=profile.get("password"),
            verify_ssl=profile.get("verify_tls"),
            timeout=api_timeout
        )
