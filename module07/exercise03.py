import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="Secret_123", database="world")

cur = conn.cursor()

cur.execute("""
    insert into employees values 
    (NULL, "jack shephard", "tr1", 10000),       
    (NULL, "james sawyer", "tr2", 20000),       
    (NULL, "kate austen", "tr3",30000),       
    (NULL, "jin kwon", "tr4",40000)       
""")

conn.commit()
print(f"Last id is {cur.lastrowid}")
print(f"{cur.rowcount} row(s) inserted.")
