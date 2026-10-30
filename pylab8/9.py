data = [
    (2, "Aman", 22, 78),
    (3, "Priya", 20, 90),
    (4, "Rahul", 21, 65)
]

cur.executemany(
    "INSERT INTO students VALUES (%s, %s, %s, %s)",
    data
)

con.commit()
print("Multiple records inserted!")