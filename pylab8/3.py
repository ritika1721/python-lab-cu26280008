import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ritika@2005",
    database="studentdb"
)

cur = con.cursor()

cur.execute("""
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    marks FLOAT
)
""")

print("Table created successfully!")

con.close()