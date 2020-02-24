import mysql.connector as con

from constant import HOST, DB_NAME, DB_USER, DB_PASS,USERS_TABLE,TRIP_TABLE,USERS_BAL_TABLE


class Connection(object):
    def __init__(self):
        self.con = con.connect(host = HOST,database = DB_NAME,user = DB_USER,passwd = DB_PASS)

    def get_cursor(self):
        return self.con.cursor()
    def commit(self):
        self.con.commit()

class UsersTable(object):
    def __init__(self, userid=None, Name=None, Email=None, Phone=None):
        self.id = userid
        self.Name = Name
        self.Email = Email
        self.Phone = Phone
        self.con = Connection()
        self.cursor = self.con.get_cursor()

    def insert(self):
        sql_query = "INSERT INTO {}({},{},{}) VALUES(%s,%s,%s)"
        raw_sql= sql_query.format(USERS_TABLE,"Name","Email","Phone",self.Name, self.Email, self.Phone)
        self.cursor.execute(raw_sql,(self.Name, self.Email, self.Phone))
        self.con.commit()

    def get_user(self):
        sql_query = "SELECT * FROM {} WHERE userid={}"
        raw_query = sql_query.format(USERS_TABLE, self.id)
        self.cursor.execute(raw_query)
        return self.cursor.fetchone()

class TripTable(object):
    def __init__(self,id=None,Name=None):
        self.id = id
        self.Name = Name
        self.con = Connection()
        self.cursor = self.con.get_cursor()

    def insert(self):
        sql_query = "INSERT INTO {}({}) VALUES(%s)"
        raw_query = sql_query.format(TRIP_TABLE,"trip_name")
        print(raw_query)
        self.cursor.execute(raw_query,(self.Name,))
        self.con.commit()

    def get_trip(self):
        sql_query = "SELECT * FROM {} WHERE tripid={}"
        raw_query = sql_query.format(TRIP_TABLE, self.id)
        self.cursor.execute(raw_query)
        return self.cursor.fetchone()

class Usersbalance(object):
    def __init__(self,Balanceid=None,Balance=None,userid=None,tripid=None):
        self.balanceid = Balanceid
        self.balance = Balance
        self.userid = userid
        self.tripid = tripid
        self.con = Connection()
        self.cursor = self.con.get_cursor()

    def insert(self):
        sql_query = "INSERT INTO {}({},{},{}) VALUES(%s,%s,%s)"
        raw_sql = sql_query.format(USERS_BAL_TABLE,"Balance","userid","tripid")
        self.cursor.execute(raw_sql,(self.balance,self.userid,self.tripid))
        self.con.commit()
