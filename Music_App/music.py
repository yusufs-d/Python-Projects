import sqlite3
import time
class Database:
    def __init__(self):
        self.createdatabase()
        self.createtable()
    def createdatabase(self):
        self.connection = sqlite3.connect("music.db")
        self.cursor = self.connection.cursor()

    def createtable(self):
        query = "create table if not exists musics (Music_Name TEXT, Minute INT,Second INT,Date_Of_Upload TEXT )"
        self.cursor.execute(query)

class Music:
    def __init__(self):
       self.database = Database()


    def display_musics(self):
        query = "select * from musics"
        self.database.cursor.execute(query)
        musics = self.database.cursor.fetchall()
        for i in range(len(musics)):
            print("Music Name: {}\nTime: {}:{}\nDate Of Upload: {}"
                  "\n******************************************"
                  .format(musics[i][0],musics[i][1],musics[i][2],musics[i][3]))
    def add_music(self,name,minute,second,date):
        query = "insert into musics Values(?,?,?,?)"
        self.database.cursor.execute(query,(name,minute,second,date))
        self.database.connection.commit()
    def delete_music(self,name):
        query1 = "select * from musics where Music_Name = ?"
        self.database.cursor.execute(query1,(name,))
        musics = self.database.cursor.fetchall()
        if len(musics) == 0:
            print("There is no music with that name !")
        else:
            query2 = "delete from musics where Music_Name = ?"
            self.database.cursor.execute(query2, (name,))
            self.database.connection.commit()


    def calculate_total_time(self):
        query = "select * from musics"
        self.database.cursor.execute(query)
        musics = self.database.cursor.fetchall()
        minutes = list()
        seconds = list()
        for i in range(len(musics)):
            minutes.append(musics[i][1])
        for i  in range(len(musics)):
            seconds.append(musics[i][2])
        total_minute = sum(seconds)//60+sum(minutes)
        extra_second = sum(seconds) % 60
        print("Total time is: {} minutes {} seconds.".format(total_minute,extra_second))

