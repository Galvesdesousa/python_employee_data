import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="ilovemv69",
    database="employee_data",
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)