import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ritika@2005",
        database="studentdb"
    )

    cur = con.cursor()
    cur.execute("SELECT * FROM students")

    for row in cur.fetchall():
        print(row)

except mysql.connector.Error as e:
    print("Database Error:", e)

finally:
    if 'con' in locals() and con.is_connected():
        con.close()