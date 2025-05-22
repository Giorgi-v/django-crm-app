import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'django_user',
    passwd = '123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")