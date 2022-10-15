import sqlite3

conn = sqlite3.connect("sqlite.db")

cur = conn.cursor()
cur.execute("INSERT INTO emp VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
    (8000, "KATO", "ANALYST", 7566, "10-1-1", 2000, None, 20))
for row in cur.execute("SELECT * FROM emp WHERE job = ?", ("ANALYST",)):
	print(row)
print("---")
cur.execute("DELETE FROM emp WHERE ename = ?", ("KATO",))
 
for row in cur.execute("SELECT * FROM emp WHERE job = ?", ("ANALYST",)):
	print(row)
	
conn.close()