cur.execute("DELETE FROM students WHERE marks < 40")

con.commit()
print("Students with marks below 40 deleted!")