import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ritika@2005"
)

cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS studentdb")

print("Database created successfully!")

con.close()