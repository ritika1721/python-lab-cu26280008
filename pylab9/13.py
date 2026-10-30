import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

cur.execute("SELECT * FROM students")

for row in cur.fetchall():
    print(row)

con.close()