# vm-reservation-system
VM Reservation System
Assume you are the administrator of a cloud which hosts some finite number of Virtual Machines. Users of your cloud can borrow or check-out VMs for use. Once they are done using it, they can check-in the VM back. Once a VM is checked in, as an administrator, you should perform some cleanup on the VM and then return it back to the pool of VMs. Some points to keep in mind:

•Implement a system that will allow your clients to check-out and check-in VMs and help you administer usage of VMs in your cloud.
•When clients need a VM for use, they will call a checkout method provided by your VM reservation system. They should get the IP of a VM they can use, along with any other details you may need.
•When clients are done using the VM, they will call a checkin method provided by your VM reservation system.
•For the sake of this assignment, you can assume cleanup of a VM means that your system will ssh into the VM using its IP and clean up all files in the /tmp directory.
•After a VM has been cleaned up, your system should add it back to the pool of VMs available for checkout by clients.
•If a client requests a VM and no VM is available to be checked out, then your system should let your clients know accordingly, so they may retry after some time.
•The same VM cannot be checked out by two clients at the same time.
•A VM checked out by one client cannot be checked in by some other client.
•If your system stops running for some reason and needs to be restarted, then it should continue to know all the information about VMs that have been already checked out and VMs that are available.

