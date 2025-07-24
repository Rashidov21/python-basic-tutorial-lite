# create_db.py
import sqlite3

conn = sqlite3.connect("faces.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    time NULL,
    status NULL,
    image_path TEXT
)
''')

conn.commit()
conn.close()
