cur.execute(
    "UPDATE students SET marks = %s WHERE id = %s",
    (95, 1)
)

con.commit()
print("Marks updated successfully!")