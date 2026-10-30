def insert_data():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    cur.execute(
        "INSERT INTO students VALUES (%s,%s,%s,%s)",
        (id, name, age, marks)
    )

    con.commit()
    print("Data inserted successfully!")


def fetch_data():
    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)


insert_data()
fetch_data()