import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

cur.execute("SELECT COUNT(*) FROM students")

result = cur.fetchone()

print("Total records:", result[0])

con.close()