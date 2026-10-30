students = [
    [1, "Riya", 85],
    [2, "Aman", 90],
    [3, "Priya", 78]
]

roll = int(input("Enter roll number: "))

for s in students:
    if s[0] == roll:
        students.remove(s)
        print("Record deleted successfully!")
        break
else:
    print("Student not found!")

print(students)