# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action
from proxmoxer import ProxmoxAPI

LOG = logging.getLogger(__name__)


class ProxmoxAction(Action):
    def __init__(self, config, timeout=5):
        super().__init__(config)
        self.config = config

    def run(self, profile_name):
        super().run()
        profile = self.config.get("default_profile")

        if not profile:
            raise ValueError("A default profile must be set in the pack configuration.")

        self.proxmox = ProxmoxAPI(
            profile.get("host"),
            user=profile.get("username") + "@" + profile.get("auth_realm"),
            password=profile.get("password"),
            verify_ssl=profile.get("verify_tls"),
        )

        raise NotImplementedError
