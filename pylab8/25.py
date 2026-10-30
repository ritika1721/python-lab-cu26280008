cur.execute("""
SELECT age, COUNT(*)
FROM students
GROUP BY age
""")

for row in cur.fetchall():
    print("Age:", row[0], "Students:", row[1])