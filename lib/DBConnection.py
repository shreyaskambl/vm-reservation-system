import sys, mysql.connector

class DBConnection:
    def __init__(self, host=None, user=None, passwd=None, database=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database

    def connectdb(self):
        try:
            mydb = mysql.connector.connect(host=self.host, user=self.user, passwd=self.passwd, database=self.database)
            return (mydb)
        except:
            print ("Connection Failed")
            sys.exit()