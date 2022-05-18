import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="world")

cur = conn.cursor()

cur.execute("""
    delete from employees where salary > 25000       
""")

conn.commit()
print(f"{cur.rowcount} row(s) deleted.")
