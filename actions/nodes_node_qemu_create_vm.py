import json
from packlib.base import ProxmoxAction


class NodesNodeQemuCreateVmAction(ProxmoxAction):
    """
    Create or restore a virtual machine.
    """

    def run(self, node, vmid, acpi=None, affinity=None, agent=None, arch=None, archive=None, args=None, audio0=None, autostart=None, balloon=None, bios=None, boot=None, bootdisk=None, bwlimit=None, cdrom=None, cicustom=None, cipassword=None, citype=None, ciuser=None, cores=None, cpu=None, cpulimit=None, cpuunits=None, description=None, efidisk0=None, force=None, freeze=None, hookscript=None, hostpci_list=None, hotplug=None, hugepages=None, ide_list=None, ipconfig_list=None, ivshmem=None, keephugepages=None, keyboard=None, kvm=None, live_restore=None, localtime=None, lock=None, machine=None, memory=None, migrate_downtime=None, migrate_speed=None, name=None, nameserver=None, net_list=None, numa=None, numa_list=None, onboot=None, ostype=None, parallel_list=None, pool=None, protection=None, reboot=None, rng0=None, sata_list=None, scsi_list=None, scsihw=None, searchdomain=None, serial_list=None, shares=None, smbios1=None, smp=None, sockets=None, spice_enhancements=None, sshkeys=None, start=None, startdate=None, startup=None, storage=None, tablet=None, tags=None, tdf=None, template=None, tpmstate0=None, unique=None, unused_list=None, usb_list=None, vcpus=None, vga=None, virtio_list=None, vmgenid=None, vmstatestorage=None, watchdog=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["acpi", acpi, "boolean"],
            ["affinity", affinity, "string"],
            ["agent", agent, "string"],
            ["arch", arch, "string"],
            ["archive", archive, "string"],
            ["args", args, "string"],
            ["audio0", audio0, "string"],
            ["autostart", autostart, "boolean"],
            ["balloon", balloon, "integer"],
            ["bios", bios, "string"],
            ["boot", boot, "string"],
            ["bootdisk", bootdisk, "string"],
            ["bwlimit", bwlimit, "integer"],
            ["cdrom", cdrom, "string"],
            ["cicustom", cicustom, "string"],
            ["cipassword", cipassword, "string"],
            ["citype", citype, "string"],
            ["ciuser", ciuser, "string"],
            ["cores", cores, "integer"],
            ["cpu", cpu, "string"],
            ["cpulimit", cpulimit, "number"],
            ["cpuunits", cpuunits, "integer"],
            ["description", description, "string"],
            ["efidisk0", efidisk0, "string"],
            ["force", force, "boolean"],
            ["freeze", freeze, "boolean"],
            ["hookscript", hookscript, "string"],
            ["hostpci[n]", hostpci_list, "string"],
            ["hotplug", hotplug, "string"],
            ["hugepages", hugepages, "string"],
            ["ide[n]", ide_list, "string"],
            ["ipconfig[n]", ipconfig_list, "string"],
            ["ivshmem", ivshmem, "string"],
            ["keephugepages", keephugepages, "boolean"],
            ["keyboard", keyboard, "string"],
            ["kvm", kvm, "boolean"],
            ["live-restore", live_restore, "boolean"],
            ["localtime", localtime, "boolean"],
            ["lock", lock, "string"],
            ["machine", machine, "string"],
            ["memory", memory, "integer"],
            ["migrate_downtime", migrate_downtime, "number"],
            ["migrate_speed", migrate_speed, "integer"],
            ["name", name, "string"],
            ["nameserver", nameserver, "string"],
            ["net[n]", net_list, "string"],
            ["node", node, "string"],
            ["numa", numa, "boolean"],
            ["numa[n]", numa_list, "string"],
            ["onboot", onboot, "boolean"],
            ["ostype", ostype, "string"],
            ["parallel[n]", parallel_list, "string"],
            ["pool", pool, "string"],
            ["protection", protection, "boolean"],
            ["reboot", reboot, "boolean"],
            ["rng0", rng0, "string"],
            ["sata[n]", sata_list, "string"],
            ["scsi[n]", scsi_list, "string"],
            ["scsihw", scsihw, "string"],
            ["searchdomain", searchdomain, "string"],
            ["serial[n]", serial_list, "string"],
            ["shares", shares, "integer"],
            ["smbios1", smbios1, "string"],
            ["smp", smp, "integer"],
            ["sockets", sockets, "integer"],
            ["spice_enhancements", spice_enhancements, "string"],
            ["sshkeys", sshkeys, "string"],
            ["start", start, "boolean"],
            ["startdate", startdate, "string"],
            ["startup", startup, "string"],
            ["storage", storage, "string"],
            ["tablet", tablet, "boolean"],
            ["tags", tags, "string"],
            ["tdf", tdf, "boolean"],
            ["template", template, "boolean"],
            ["tpmstate0", tpmstate0, "string"],
            ["unique", unique, "boolean"],
            ["unused[n]", unused_list, "string"],
            ["usb[n]", usb_list, "string"],
            ["vcpus", vcpus, "integer"],
            ["vga", vga, "string"],
            ["virtio[n]", virtio_list, "string"],
            ["vmgenid", vmgenid, "string"],
            ["vmid", vmid, "integer"],
            ["vmstatestorage", vmstatestorage, "string"],
            ["watchdog", watchdog, "string"],
            
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
            f"nodes/{node}/qemu",
            **proxmox_kwargs
        )
        