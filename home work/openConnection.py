import mysql.connector

def getconnection():
    db=mysql.connector.connect(host="localhost",user="root",passwd="sajay",database="luminar")
    return db