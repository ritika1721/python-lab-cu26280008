while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks: "))

        cur.execute(
            "INSERT INTO students VALUES (%s,%s,%s,%s)",
            (id, name, age, marks)
        )

        con.commit()
        print("Student added successfully!")

    elif choice == 2:
        cur.execute("SELECT * FROM students")

        for row in cur.fetchall():
            print(row)

    elif choice == 3:
        id = int(input("Enter Student ID: "))
        marks = float(input("Enter new marks: "))

        cur.execute(
            "UPDATE students SET marks=%s WHERE id=%s",
            (marks, id)
        )

        con.commit()
        print("Student updated successfully!")

    elif choice == 4:
        id = int(input("Enter Student ID: "))

        cur.execute(
            "DELETE FROM students WHERE id=%s",
            (id,)
        )

        con.commit()
        print("Student deleted successfully!")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

con.close()