import mysql.connector

"""
    1. Connection-oriented
    2. Flat Model: 1 Connection --> 1 TX
    3. Isolation Level: READ UNCOMMITTED, READ COMMITTED (default), REPEATABLE READ, SERIALIZABLE (ANSI) 
"""
conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="world")

cur = conn.cursor()

cur.execute("""
   set session transaction isolation level repeatable read
""")

cur.execute("""
    update employees set salary = salary * 2       
""")

conn.commit()
print(f"{cur.rowcount} row(s) updated.")
