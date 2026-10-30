import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="studentdb"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
roll INT PRIMARY KEY,
name VARCHAR(50),
marks FLOAT
)
""")

print("Table created successfully!")

con.close()