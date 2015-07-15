import sqlite3 
with sqlite3.connect("mydb.db") as con:
	cur = con.cursor()
	cur.execute('''CREATE TABLE contacts(name TEXT, phone INT)''')
	cur.execute('''INSERT INTO contacts VALUES("Ebowe Blessing", 08062201524)''')
	cur.execute('''INSERT INTO contacts VALUES("Ebowe Sarah", 08055227325)''')
	

