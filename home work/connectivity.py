import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

con = MySQLdb.connect("localhost","root","Password@123","NEW")
cur = con.cursor()

sql= "SELECT * FROM WORKERS  where id<=%d" % 10

cur.execute(sql)
rows=cur.fetchall()
print(rows)
for row in rows:
    f=row[0]
    print(f)
    print("the identity no = %d" % (f))

