cur.execute("""
CREATE TABLE courses (
    id INT PRIMARY KEY,
    course_name VARCHAR(50)
)
""")

data = [
    (1, "Python"),
    (2, "Java"),
    (3, "C++")
]

cur.executemany(
    "INSERT INTO courses VALUES (%s, %s)",
    data
)

con.commit()
print("Courses created and data inserted!")