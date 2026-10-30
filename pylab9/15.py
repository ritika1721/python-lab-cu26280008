import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

roll = int(input("Enter roll number: "))
marks = float(input("Enter new marks: "))

cur.execute(
    "UPDATE students SET marks=%s WHERE roll=%s",
    (marks, roll)
)

con.commit()

print("Marks updated successfully!")

con.close()