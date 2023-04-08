# imorting connectors of DB

import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1@bitch2"
)

#  creating cursor object
cursorObject = database.cursor()

# creating DB
cursorObject. execute("CREATE DATABASE Malipo_db")

print("DB created")

