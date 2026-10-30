import csv

f = open("student.csv", "a", newline="")
w = csv.writer(f)

w.writerow(["Neha", 95])

f.close()

print("Record added successfully")