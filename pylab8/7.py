cur.execute("SHOW TABLES")

tables = cur.fetchall()

if ("students",) in tables:
    print("Table exists")
else:
    print("Table does not exist")