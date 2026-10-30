import csv

f = open("student.csv", "r")
r = csv.reader(f)

next(r)

total = 0
count = 0

for row in r:
    total = total + int(row[1])
    count = count + 1

print("Average:", total / count)

f.close()