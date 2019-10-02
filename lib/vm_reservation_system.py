from lib.VMReservation import VMReservation
from lib.DBConnection import DBConnection
import sys

def menu ():
    print ('''\nProvide Input Number for the operation
           [1] Checkout a VM
           [2] CheckIn a VM 
           [3] Exit''')

def login():
    f = open("users.txt", "r")
    userscontent = f.readlines()
    f.close()
    username=input("Enter username : ").strip()
    password=input("Enter password : ").strip()
    for usercontent in userscontent:
        user, passwd = usercontent.split(":")
        if user.strip()==username and passwd.strip()==password:
            print("Welcome - Access Granted")
            return(user)
    print ("Invalid username and password")
    sys.exit()
    

def run_vm_reservation_system ():
    db = DBConnection(host="localhost", user="dbuser", passwd="dbpasswd", database="reservation")
    mydb = db.connectdb()
    vm_reservation = VMReservation(mydb)
    user = login()
    loop = 1
    while loop == 1:
        menu()
        choice = int(input())

        if choice == 1:
            vm_checkout(vm_reservation, user)

        if choice == 2:
            vm_checkin(vm_reservation, user)

        if choice == 3:
            sys.exit()

def vm_checkin (vm_reservation, user):
    vm_allocation_list = vm_reservation.get_user_vm_allocation_status(user)
    if (any(vm_allocation_list)):
        allocation = [ x[0] for x in vm_allocation_list ]
        print ("VMs allocated to user " + user + " : " + str(allocation))
        checkin_vm = input("\nProvide the VM name from below list that you want to checkin : ")
        vm_reservation.cleanup(checkin_vm)
        vm_reservation.checkin(checkin_vm, user)
    else:
        print ("\nYou have no VM to checkin\n")

def vm_checkout (vm_reservation, user):
    vm_status_list = vm_reservation.get_checkin_status()
    if (any(vm_status_list)):
        vm_reservation.checkout(vm_status_list.pop(), user)
    else:
        print ("All resources are occupied. VM cannot be provisioned at the moment. Please try later")