import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO entry (title, description, status) VALUES (?, ?, ?)",
            ('First Post', 'Content for the first post', 1)
            )

cur.execute("INSERT INTO entry (title, description, status) VALUES (?, ?, ?)",
            ('Second Post', 'Content for the second post', 0)
            )

connection.commit()
connection.close()
