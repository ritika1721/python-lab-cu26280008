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
    "DELETE FROM students WHERE roll=%s",
    (roll,)
)

con.commit()

print("Record deleted successfully!")

con.close()