import json
from packlib.base import ProxmoxAction


class NodesNodeQemuVmidConfigUpdateVmAction(ProxmoxAction):
    """
    Set virtual machine options (synchrounous API) - You should consider using the POST method instead for any actions involving hotplug or storage allocation.
    """

    def run(self, node, vmid, acpi=None, agent=None, arch=None, args=None, audio0=None, autostart=None, balloon=None, bios=None, boot=None, bootdisk=None, cdrom=None, cicustom=None, cipassword=None, citype=None, ciuser=None, cores=None, cpu=None, cpulimit=None, cpuunits=None, delete=None, description=None, digest=None, efidisk0=None, force=None, freeze=None, hookscript=None, hostpci_list=None, hotplug=None, hugepages=None, ide_list=None, ipconfig_list=None, ivshmem=None, keephugepages=None, keyboard=None, kvm=None, localtime=None, lock=None, machine=None, memory=None, migrate_downtime=None, migrate_speed=None, name=None, nameserver=None, net_list=None, numa=None, numa_list=None, onboot=None, ostype=None, parallel_list=None, protection=None, reboot=None, revert=None, rng0=None, sata_list=None, scsi_list=None, scsihw=None, searchdomain=None, serial_list=None, shares=None, skiplock=None, smbios1=None, smp=None, sockets=None, spice_enhancements=None, sshkeys=None, startdate=None, startup=None, tablet=None, tags=None, tdf=None, template=None, unused_list=None, usb_list=None, vcpus=None, vga=None, virtio_list=None, vmgenid=None, vmstatestorage=None, watchdog=None, profile_name=None):
        super().run(profile_name)

        # Only include non None arguments to pass through to proxmox api.
        proxmox_kwargs = {}
        for api_arg in [
            ["acpi", acpi, "boolean"],
            ["agent", agent, "string"],
            ["arch", arch, "string"],
            ["args", args, "string"],
            ["audio0", audio0, "string"],
            ["autostart", autostart, "boolean"],
            ["balloon", balloon, "integer"],
            ["bios", bios, "string"],
            ["boot", boot, "string"],
            ["bootdisk", bootdisk, "string"],
            ["cdrom", cdrom, "string"],
            ["cicustom", cicustom, "string"],
            ["cipassword", cipassword, "string"],
            ["citype", citype, "string"],
            ["ciuser", ciuser, "string"],
            ["cores", cores, "integer"],
            ["cpu", cpu, "string"],
            ["cpulimit", cpulimit, "number"],
            ["cpuunits", cpuunits, "integer"],
            ["delete", delete, "string"],
            ["description", description, "string"],
            ["digest", digest, "string"],
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
            ["protection", protection, "boolean"],
            ["reboot", reboot, "boolean"],
            ["revert", revert, "string"],
            ["rng0", rng0, "string"],
            ["sata[n]", sata_list, "string"],
            ["scsi[n]", scsi_list, "string"],
            ["scsihw", scsihw, "string"],
            ["searchdomain", searchdomain, "string"],
            ["serial[n]", serial_list, "string"],
            ["shares", shares, "integer"],
            ["skiplock", skiplock, "boolean"],
            ["smbios1", smbios1, "string"],
            ["smp", smp, "integer"],
            ["sockets", sockets, "integer"],
            ["spice_enhancements", spice_enhancements, "string"],
            ["sshkeys", sshkeys, "string"],
            ["startdate", startdate, "string"],
            ["startup", startup, "string"],
            ["tablet", tablet, "boolean"],
            ["tags", tags, "string"],
            ["tdf", tdf, "boolean"],
            ["template", template, "boolean"],
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

        return self.proxmox.put(
            f"nodes/{node}/qemu/{vmid}/config",
            **proxmox_kwargs
        )
        