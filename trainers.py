import sqlite3
from sqlite3.dbapi2 import Cursor
import pandas as pd
import sqlite3
class Trainer:
    
    def __init__(self):
        pass
    def create(self):
        # Connect to sqlite database
        conn = sqlite3.connect('computer-pride.db')
        # cursor object
        cursor = conn.cursor()
        # drop query
    
        createTb="""CREATE TABLE TRAINER(
        ID INT PRIMARY KEY NOT NULL,
        TRAINERNAME CHAR(20) NOT NULL,
        USERNAME CHAR(20) NOT NULL,  
        PASSWORD CHAR(20) )"""
        cursor.execute(createTb)
        conn.commit()
        conn.close()

    def insert(self):
        conn = sqlite3.connect('computer-pride.db')

        conn.execute("INSERT INTO TRAINER (ID,TRAINERNAME, USERNAME,PASSWORD) "
             "VALUES (1, 'John','ADMIN', '12345')")

        conn.execute("INSERT INTO TRAINER (ID,TRAINERNAME, USERNAME,PASSWORD) "
             "VALUES (2, 'James','ADMIN', '12345')")

        query = ('INSERT INTO TRAINER (ID,TRAINERNAME, USERNAME,PASSWORD) '
             "VALUES (3, 'Alex','ADMIN', '12345')")
        conn.execute(query)
        conn.commit()
        conn.close()
    def retriveall(self):
        conn = sqlite3.connect('computer-pride.db')
        cursor = conn.execute("SELECT * from TRAINER")
        print(cursor.fetchall())
    def retriveById(self,id):
        conn = sqlite3.connect('computer-pride.db')
        cursor =conn.execute("SELECT ID FROM TRAINER WHERE id="+str(id))
        print(cursor.fetchall())

    
    def update(self,id):
        conn = sqlite3.connect('computer-pride.db')
        conn.execute("UPDATE TRAINER set TRAINERNAME = 'JAMES' where ID = 1")
        conn.commit()
        cursor = conn.execute("SELECT * from STUDENT")
        print(cursor.fetchall())
        conn.close()
    def delete(self,id):
        conn = sqlite3.connect('students.db')
        conn.execute("DELETE from TRAINER where ID = 1;")
        conn.commit()
        cursor = conn.execute("SELECT * from STUDENT")
        print(cursor.fetchall())
        conn.close()
    create()
    insert()




     
