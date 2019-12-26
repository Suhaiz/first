import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

con=MySQLdb.connect("localhost","root","Password@123","NEW")
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS WORKERS")

sql="CREATE TABLE WORKERS(ID INT,NAME VARCHAR(20),AGE INT)"
work="INSERT INTO WORKERS(ID,NAME,AGE) VALUES('%d','%s','%d')"%(10,'x',7)

cur.execute(sql)
cur.execute(work)

con.commit()

con.close()
#
#


# sql = """INSERT INTO WORKERS(ID,
#          NAME, AGE)
#          VALUES (1, 'Mohan', 20)"""
# # try:
#    # Execute the SQL command
# cur.execute(sql)
#    # Commit your changes in the database
# con.commit()
# # except:
# #    # Rollback in case there is any error
# #    con.rollback()
#
# # disconnect from server
# con.close()



#################the first step is
#1package install
#2connection establish
#3create cursor object