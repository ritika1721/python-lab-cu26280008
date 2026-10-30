cur.execute("SHOW TABLES")

for row in cur.fetchall():
    print(row)