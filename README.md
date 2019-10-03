# vm-reservation-system
VM Reservation System

Pre-requisite:

DATA SETUP
1. Install MySQL server (version 8.0 at the time of time documentation) on localhost where you intend to run this script.
2. At the time of installation, create user 'dbuser' and set a password for it (eg. dbpasswd)
3. Grant all privileges to this user (dbuser). Eg. GRANT ALL TO 'dbuser@localhost';
4. Connect to MySQL server using dbuser account
5. Create a database 'reservation' (Eg. CREATE DATABASE RESERVATION)
6. Change scope to reservation DB (Eg. USE DATABASE RESERVATION)
7. Create 2 tables; VM and USER_VM_ALLOCATION
   a. CREATE TABLE VM (NAME VARCHAR(20), IP INT UNSIGNED, STATUS VARCHA(10))   #this table resembles pool of VMs
   b. CREATE TABLE USER_VM_ALLOCATION (NAME VARCHAR(20), VM_NAME VARCHAR(20))  #this rable resembles user allocation of VMs
8. Populate table 'VM' with VM details with default status as 'checkin' (as not VMs are checked out yet)
   a. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm1', INET_ATON(10.30.4.1), "checkin")
   b. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm2', INET_ATON(10.30.4.2), "checkin")
   c. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm3', INET_ATON(10.30.4.3), "checkin")
   d. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm4', INET_ATON(10.30.4.4), "checkin")
   e. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm5', INET_ATON(10.30.4.5), "checkin")
   f. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm6', INET_ATON(10.30.4.6), "checkin")
   g. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm7', INET_ATON(10.30.4.7), "checkin")
   h. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm8', INET_ATON(10.30.4.8), "checkin")
   i. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm8', INET_ATON(10.30.4.9), "checkin")
   j. INSERT INTO VM(NAME, IP, STATUS) VALUES ('vm10', INET_ATON(10.30.4.10), "checkin")

RUNTIME SETUP:
1. Install Python version 3.7
2. Install mysql-connector-python using pip (Eg. python -m pip3 install mysql-connector-python) 

Script:
Run python script ./runner.py
To login; use user1/passwd1 or user2/passwd2
Script run in interactive fashion using menu.
