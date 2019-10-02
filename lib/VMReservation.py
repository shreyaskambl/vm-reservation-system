import os

class VMReservation:
    def __init__(self, mydb):
        self.vm_upd_stmt = "UPDATE VM SET STATUS = %s WHERE NAME = %s"
        self.user_vm_alloc_insert_stmt = "INSERT INTO USER_VM_ALLOCATION(name, vm_name) VALUES (%s, %s)"
        self.user_vm_alloc_delete_stmt = "DELETE FROM USER_VM_ALLOCATION WHERE NAME = %s and VM_NAME = %s"
        self.mydb = mydb

    def checkout(self, vm, user):
        mycursor = self.mydb.cursor()
        vm_name = [("checkout", vm[0])]
        mycursor.executemany(self.vm_upd_stmt, vm_name)
        user_vm_alloc = [(user, vm[0])]
        mycursor.executemany(self.user_vm_alloc_insert_stmt, user_vm_alloc)
        self.mydb.commit()
        print ("\nVM " + vm[0] + " checkout completed. Connect to VM using IP " + str(vm[1]))

    def checkin(self, vm, user):
        mycursor = self.mydb.cursor()
        vm_name = [("checkin", vm)]
        mycursor.executemany(self.vm_upd_stmt, vm_name)
        user_vm_alloc = [(user, vm)]
        mycursor.executemany(self.user_vm_alloc_delete_stmt, user_vm_alloc)
        self.mydb.commit()
        print ("\nVM " + vm + " checkin completed.")

    def get_checkin_status(self):
        stmt = 'SELECT NAME, INET_NTOA(IP) from VM WHERE STATUS = "checkin"'
        mycursor = self.mydb.cursor()
        mycursor.execute(stmt)
        return(mycursor.fetchall())

    def get_user_vm_allocation_status(self, user):
        stmt = 'SELECT VM_NAME from USER_VM_ALLOCATION WHERE NAME = "' + user + '"'
        mycursor = self.mydb.cursor()
        mycursor.execute(stmt)
        return(mycursor.fetchall())

    def cleanup (self, vm):
        cmd = "ssh root@" + vm + " ' if [ -d /tmp]; then rm -rf /tmp*; fi"
        print (cmd)
        try:
            print ("Cleanup VM is completed")
            #os.system(cmd)  ##disabling as there is no real VM
        except:
            print ("Cleanup failed")