students = [
    [1, "Riya", 85],
    [2, "Aman", 90],
    [3, "Priya", 78]
]

name = input("Enter student name: ")

for s in students:
    if s[1] == name:
        print("Student found:", s)
        break
else:
    print("Student not found!")