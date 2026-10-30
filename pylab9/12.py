import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

roll = int(input("Enter roll number: "))
name = input("Enter name: ")
marks = float(input("Enter marks: "))

cur.execute(
    "INSERT INTO students VALUES(%s,%s,%s)",
    (roll, name, marks)
)

con.commit()

print("Record inserted successfully!")

con.close()