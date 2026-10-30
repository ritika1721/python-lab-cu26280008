students = [
    "1 Riya 85",
    "2 Aman 90",
    "3 Priya 78"
]

file = open("students.txt", "w")

for s in students:
    file.write(s + "\n")

file.close()

file = open("students.txt", "r")

print("Student Records:")

for line in file:
    print(line.strip())

file.close()