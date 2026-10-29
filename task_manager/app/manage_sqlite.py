import sqlite3

con = sqlite3.connect('tasks_manager.db')
cur = con.cursor()
# cur.execute('CREATE TABLE Tasks(id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, completed Bool)')
# cur.execute('INSERT INTO Tasks(task, completed) VALUES(?,?)', ('renmerry', False))
# cur.execute('INSERT INTO Tasks(task, completed) VALUES(?,?)', ('renmerry1', True))



for s in cur.execute('Select completed from Tasks').fetchall():
    print(s)

con.commit()
con.close()