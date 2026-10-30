import csv

f = open("student.csv", "r")
r = csv.reader(f)

for row in r:
    print(row)

f.close()