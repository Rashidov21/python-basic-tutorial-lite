# import sqlite3
# pip install Faker
# SQL - malumotlar omborini boshqarish tili 
# .sql, .db - ombor fayllari

# ombor faylini hosil qilish yoki unga ulanish
# conn = sqlite3.connect("users.db", check_same_thread=False)

# omborni boshqarish uchun cursor - ko'rsatkich
# cur = conn.cursor()

# sql buyruqlarni bajarish uchun
# cur.execute(
#     """CREATE TABLE users(
#         id INT PRIMARY KEY,
#         name TEXT,
#         age INT
#     );"""
# )
# table ga malumot yozish
# cur.execute("""INSERT INTO users VALUES(1,'John',23);""")
# conn.commit() # bu bazaga ozgarishlarni tasdiqlash
# print("Success!")

# import sqlite3
# from faker import Faker

# db_connect = sqlite3.connect("fake_users.db", check_same_thread=False)
# db_cursor = db_connect.cursor()

# fake = Faker()

# 1-ish
# try:
#     db_cursor.execute("""
#     CREATE TABLE customers(
#                       id INT PRIMARY KEY,
#                       name TEXT,
#                       surname TEXT,
#                       phone TEXT,
#                       email TEXT,
#                       country TEXT,
#                       city TEXT,
#                       address TEXT);""")
# except sqlite3.DatabaseError as e:
#     print(e)

# 2-ish
# try:
#     for i in range(51,401):
#         db_cursor.execute(f"""
#             INSERT INTO customers 
#             VALUES({i},'{fake.name().split(" ")[0]}','{fake.name().split(" ")[1]}',
#             '{fake.phone_number()}','{fake.email()}','{fake.country()}','{fake.city()}','{fake.address()}');""")
# except sqlite3.DatabaseError as e:
#     print(e)
# else:
#     db_connect.commit()


# # 3-ish
# data = db_cursor.execute("SELECT * FROM customers")
# data = db_cursor.execute("SELECT name FROM customers WHERE country='Uzbekistan'")
# print(data.fetchall())




import sqlite3

db_connect = sqlite3.connect("fake_users.db", check_same_thread=False)
db_cursor = db_connect.cursor()

# CRUD - Create,Read,Update,Delete
# Create - INSERT INTO <table name> VALUES(value1,value2);
# Read - SELECT 
# data = db_cursor.execute("SELECT name,surname FROM customers WHERE id=25")
# print(data.fetchall()) # [('Jennifer', 'Ferguson')]

# data = db_cursor.execute("SELECT name,surname FROM customers WHERE country LIKE 'A%'")
# print(data.fetchall())
# # ikita qiymat orasidagilarni olish 
# data = db_cursor.execute("SELECT title FROM books WHERE price  BETWEEN 35000 AND 100000")
# print(data.fetchall())
# data = db_cursor.execute("DELETE FROM customers WHERE name='Barry'")
# data = db_cursor.execute("UPDATE customers SET name='James', surname='Rodriguez' WHERE id=1")
# db_connect.commit()
# data = db_cursor.execute("SELECT name FROM customers ORDER BY name DESC")
# data = db_cursor.execute("SELECT name FROM customers WHERE name LIKE 'K%' AND country='Uzbekistan' ")
# print(data.fetchall())
# data = db_cursor.execute("SELECT name,surname FROM customers WHERE country='Macao' OR country='Iran' ")
# print(data.fetchall())
# data = db_cursor.execute("SELECT name,surname FROM customers WHERE NOT country='Iran' ")
# print(data.fetchall())