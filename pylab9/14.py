import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

roll = int(input("Enter roll number: "))

cur.execute(
    "SELECT * FROM students WHERE roll=%s",
    (roll,)
)

result = cur.fetchone()

if result:
    print("Student found:", result)
else:
    print("Student not found!")

con.close()