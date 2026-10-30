cur.execute(
    "UPDATE students SET name = %s WHERE id = %s",
    ("Anjali", 2)
)

con.commit()
print("Name updated successfully!")