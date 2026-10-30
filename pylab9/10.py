file = "students.txt"

while True:
    print("\n1. Add")
    print("2. View")
    print("3. Modify")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        data = input("Enter student record: ")

        f = open(file, "a")
        f.write(data + "\n")
        f.close()

        print("Record added!")

    elif choice == 2:
        f = open(file, "a+")
        f.seek(0)

        for line in f:
            print(line.strip())

        f.close()

    elif choice == 3:
        old = input("Enter old record: ")
        new = input("Enter new record: ")

        f = open(file, "r")
        data = f.read()
        f.close()

        data = data.replace(old, new)

        f = open(file, "w")
        f.write(data)
        f.close()

        print("Record modified!")

    elif choice == 4:
        old = input("Enter record to delete: ")

        f = open(file, "r")
        data = f.readlines()
        f.close()

        f = open(file, "w")

        for line in data:
            if line.strip() != old:
                f.write(line)

        f.close()
        print("Record deleted!")

    elif choice == 5:
        break

    else:
        print("Invalid choice!")