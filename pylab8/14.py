cur.execute("SELECT COUNT(*) FROM students")

result = cur.fetchone()

print("Total records:", result[0])