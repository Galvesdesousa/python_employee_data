import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="ilovemv69"
)

if db.is_connected():
    print("Database Connected")