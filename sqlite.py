import sqlite3
connection=sqlite3.connect('my_database.db')
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE students(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
grade TEXT
)''')
connection.commit()