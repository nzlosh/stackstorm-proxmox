import time
import os
import urllib3

from packlib.base import ProxmoxAction

# Import proxmox actions needed for this action
from nodes_node_qemu_vmid_clone_clone_vm import NodesNodeQemuVmidCloneCloneVmAction
from nodes_node_tasks_upid_status_read_task_status import (
    NodesNodeTasksUpidStatusReadTaskStatusAction,
)


def duration(start):
    return time.time() - start


class NodesNodeQemuVmidCloneCloneVmWaitCompletionAction(ProxmoxAction):
    """
    newid = the new VM id that will be created.
    node = the node to create the new VM on.
    vmid = the template vm id.
    """

    def run(
        self,
        newid,
        node,
        vmid,
        bwlimit=None,
        description=None,
        prox_format=None,
        full=None,
        name=None,
        pool=None,
        snapname=None,
        storage=None,
        target=None,
        profile_name=None,
        api_timeout=5,
        clone_timeout=120,
        ignore_ssl=False,
    ):
        if ignore_ssl:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        start = time.time()

        clone_vm = NodesNodeQemuVmidCloneCloneVmAction(self.config)
        upid = clone_vm.run(
            newid,
            node,
            vmid,
            bwlimit=bwlimit,
            description=description,
            prox_format=prox_format,
            full=full,
            name=name,
            pool=pool,
            snapname=snapname,
            storage=storage,
            target=target,
            profile_name=profile_name,
            api_timeout=api_timeout,
        )

        clone_end = time.time()
        task_state = "running"
        task = NodesNodeTasksUpidStatusReadTaskStatusAction(self.config)
        while task_state == "running":
            res = task.run(
                node=node,
                upid=upid,
                profile_name=profile_name, api_timeout=api_timeout
            )
            task_state = res["status"]
            exit_state = res.get("exitstatus", "n/a")
            time.sleep(1)
            if int(duration(start)) > clone_timeout:
                break

        return (exit_state == "OK", {"upid": upid, "task": res, "duration": duration(start)})
