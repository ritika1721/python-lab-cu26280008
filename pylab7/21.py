import csv

f = open("student.csv", "w", newline="")
w = csv.writer(f)

w.writerow(["Name", "Marks"])
w.writerow(["Riya", 85])
w.writerow(["Aman", 90])

f.close()

print("CSV file created")