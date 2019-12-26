# import sqlite3 as lite
# import sys
#
# con=lite.connect('test.db')
# cur=con.cursor()
# cur.executescript("""
#                   DROP TABLE IF EXISTS Cars;
#                   CREATE TABLE Cars(ID INT, NAME TEXT,PRICE INT);
#                   INSERT INTO CARS VALUES(1,'AUDI',5444);
#                   """)
# con.commit()
# if con:
#     con.close()
#
# con1=lite.connect('test.db')
# cur1=con1.cursor()
# cur1.execute("SELECT * FROM Cars")
# rows=cur1.fetchall()
#
# for i in rows:
#     print(i)
#
# con.close()

import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
db = MySQLdb.connect("localhost","root","Password@123","LUMINAR" )

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)

db.close()