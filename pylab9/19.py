import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

cur.execute(
    "SELECT * FROM students ORDER BY marks DESC LIMIT 1"
)

result = cur.fetchone()

print("Highest Scoring Student:", result)

con.close()