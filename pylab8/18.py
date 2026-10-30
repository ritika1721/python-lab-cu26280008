cur.execute(
    "DELETE FROM students WHERE id = %s",
    (3,)
)

con.commit()
print("Record deleted successfully!")