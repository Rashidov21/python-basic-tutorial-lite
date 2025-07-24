import sqlite3

conn = sqlite3.connect("asaxiy_books.db", check_same_thread=False)
cur = conn.cursor()
# cur.execute(
#     """CREATE TABLE books(
#         title TEXT,
#         price TEXT,
#         url TEXT
#     );"""
# )
def write_to_db(title,price,url):
    try:
        cur.execute(f"""INSERT INTO books VALUES('{title}','{price}','{url}');""")
    except sqlite3.DatabaseError as e:
        print(e)
    else:
        conn.commit()
