cur.execute(
    "INSERT INTO students VALUES (%s, %s, %s, %s)",
    (1, "Riya", 21, 85)
)

con.commit()
print("Record inserted successfully!")