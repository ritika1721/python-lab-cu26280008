import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ritika@2005"
)

if con.is_connected():
    print("Database connected successfully!")

con.close()