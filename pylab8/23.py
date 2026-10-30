cur.execute("""
SELECT students.name, courses.course_name
FROM students
LEFT JOIN courses
ON students.course_id = courses.id
""")

for row in cur.fetchall():
    print(row)