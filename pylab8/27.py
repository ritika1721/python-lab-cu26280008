import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        cur.execute(
            "INSERT INTO students VALUES (%s, %s, %s, %s)",
            row
        )

con.commit()
print("CSV data imported successfully!")