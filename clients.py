import sqlite3

def init_db():
	conn = sqlite3.connect("clients.db")
	cur = conn.cursor()

	cur.execute('''
		CREATE TABLE IF NOT EXISTS clients (
				username TEXT PRIMARY KEY NOT NULL,
				password TEXT NOT NULL,
				firstname TEXT NOT NULL,
				lastname TEXT NOT NULL,
				patronym TEXT,
				birthdate DATE NOT NULL,
				phonenum INTEGER NOT NULL,
				email TEXT
			)
		''')
	conn.commit()
	conn.close()

def add_client(username, password, firstname, lastname, patronym, birthdate, phonenum, email):
	conn = sqlite3.connect("clients.db")
	cur = conn.cursor()

	try:
		cur.execute("INSERT INTO clients (username, password, firstname, lastname, patronym, birthdate, phonenum, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (username, password, firstname, lastname, patronym, birthdate, phonenum, email))
		conn.commit()
		return True
	except sqlite3.IntegrityError:
		return False
	finally:
		conn.close()


def validate_client(username, password):
	conn = sqlite3.connect("clients.db")
	cur = conn.cursor()

	cur.execute("SELECT * FROM clients WHERE username=? AND password=?", (username, password))
	result = cur.fetchone()
	conn.close()
	return result is not None 