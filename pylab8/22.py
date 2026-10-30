cur.execute("ALTER TABLE students ADD course_id INT")

cur.execute("UPDATE students SET course_id = 1 WHERE id = 1")
cur.execute("UPDATE students SET course_id = 2 WHERE id = 2")

con.commit()

cur.execute("""
SELECT students.name, courses.course_name
FROM students
INNER JOIN courses
ON students.course_id = courses.id
""")

for row in cur.fetchall():
    print(row)