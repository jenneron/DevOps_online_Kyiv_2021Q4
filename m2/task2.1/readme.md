# Task 2.1

## Part 1. HYPERVISORS

### 1. What are the most popular hypervisors for infrastructure virtualization?

The most popular hypervisors are:
- VMware ESXi/vSphere;
- Microsoft Hyper-V;
- Citrix XenServer;
- Oracle VirtualBox;
- Parallels Hypervisor;
- Red Hat Enterprise Virtualization;

### 2. Briefly describe the main differences of the most popular hypervisors.

There are two types of hypervisors:
- Type 1 hypervisor: hypervisors run directly on the system hardware – A “bare metal” embedded hypervisor,
- Type 2 hypervisor: hypervisors run on a host operating system that provides virtualization services, such as I/O device support and memory management.

## Part 2. WORK WITH VIRTUALBOX

### Group

![image](group.png)

### USB

![image](usb.png)

### Shared folder

![image](shared_folder.png)

### VBoxManage list

```console
$ VBoxManage list vms
"VM1_Bambura" {96a8554e-ec5a-4f99-939c-ac5cd882d503}
"VM2_Bambura" {b3c994e6-6ca0-469c-b0d2-a2f56676b337}
"VM1_Bambura (import)" {4c935e6f-933b-4878-a680-97f52aef8850}
```
