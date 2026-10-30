import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll: "))
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))

        cur.execute(
            "INSERT INTO students VALUES(%s,%s,%s)",
            (roll, name, marks)
        )

        con.commit()
        print("Student added!")

    elif choice == 2:
        cur.execute("SELECT * FROM students")

        for row in cur.fetchall():
            print(row)

    elif choice == 3:
        roll = int(input("Enter roll: "))
        marks = float(input("Enter new marks: "))

        cur.execute(
            "UPDATE students SET marks=%s WHERE roll=%s",
            (marks, roll)
        )

        con.commit()
        print("Student updated!")

    elif choice == 4:
        roll = int(input("Enter roll: "))

        cur.execute(
            "DELETE FROM students WHERE roll=%s",
            (roll,)
        )

        con.commit()
        print("Student deleted!")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

con.close()