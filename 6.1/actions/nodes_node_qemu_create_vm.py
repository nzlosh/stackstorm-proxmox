import json
from packlib.base import ProxmoxAction


class NodesNodeQemuCreateVmAction(ProxmoxAction):
    """
    Create or restore a virtual machine.
    """

    def run(self, node, vmid, acpi=True, agent=None, arch=None, archive=None, args=None, audio0=None, autostart=False, balloon=None, bios="seabios", boot="cdn", bootdisk=None, bwlimit=restore limit from datacenter or storage config, cdrom=None, cicustom=None, cipassword=None, citype=None, ciuser=None, cores=1, cpu=None, cpulimit=0, cpuunits=1024, description=None, efidisk0=None, force=None, freeze=None, hookscript=None, hostpci_list=None, hotplug="network,disk,usb", hugepages=None, ide_list=None, ipconfig_list=None, ivshmem=None, keyboard=null, kvm=True, localtime=None, lock=None, machine=None, memory=512, migrate_downtime=0.1, migrate_speed=0, name=None, nameserver=None, net_list=None, numa=False, numa_list=None, onboot=False, ostype=None, parallel_list=None, pool=None, protection=False, reboot=True, sata_list=None, scsi_list=None, scsihw="lsi", searchdomain=None, serial_list=None, shares=1000, smbios1=None, smp=1, sockets=1, spice_enhancements=None, sshkeys=None, start=False, startdate="now", startup=None, storage=None, tablet=True, tags=None, tdf=False, template=False, unique=None, unused_list=None, usb_list=None, vcpus=0, vga=None, virtio_list=None, vmgenid="1 (autogenerated)", vmstatestorage=None, watchdog=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["acpi", acpi, "boolean"],
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
            ["keyboard", keyboard, "string"],
            ["kvm", kvm, "boolean"],
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
        