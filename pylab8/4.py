cur.execute("DESC students")

for row in cur.fetchall():
    print(row)