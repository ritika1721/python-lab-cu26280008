import csv

cur.execute("SELECT * FROM students")

data = cur.fetchall()

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["ID", "Name", "Age", "Marks"])
    writer.writerows(data)

print("Data exported to CSV successfully!")