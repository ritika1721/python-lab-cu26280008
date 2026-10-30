import csv

f = open("student.csv", "r")
r = csv.reader(f)

data = list(r)

print("Rows:", len(data))
print("Columns:", len(data[0]))

f.close()