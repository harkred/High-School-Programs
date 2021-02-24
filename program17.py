import mysql.connector as sql

mydb = sql.connect(host=HOST, user=USER, passwd=PASSWD)
curse = sql.cursor()
