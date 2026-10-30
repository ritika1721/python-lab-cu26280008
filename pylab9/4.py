students = [
    [1, "Riya", 85],
    [2, "Aman", 90],
    [3, "Priya", 78]
]

roll = int(input("Enter roll number: "))
marks = int(input("Enter new marks: "))

for s in students:
    if s[0] == roll:
        s[2] = marks
        print("Marks updated successfully!")
        break
else:
    print("Student not found!")

print(students)