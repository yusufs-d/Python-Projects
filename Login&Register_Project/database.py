import sqlite3

class Database:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()
    def create_table(self):
        self.query = "create table if not exists users (Username TEXT, Password TEXT)"
        self.cursor.execute(self.query)
        self.con.commit()
    def check_login_infos(self,u_name,pw):
        self.query2 = "select * from users where Username = ? and Password = ? "
        self.cursor.execute(self.query2,(u_name,pw))
        return self.cursor.fetchall()
    def add_user(self,u_name,pw):
        self.query3 = "insert into users values (?,?)"
        self.cursor.execute(self.query3,(u_name,pw))
        self.con.commit()