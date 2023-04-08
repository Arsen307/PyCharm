import sqlite3

conection = sqlite3.connect("urok 10.sl3", 5)
cur = conection.cursor()
cur.execute("CREATE TABLE first_table (name TEXT);")
conection.commit()
conection.close()