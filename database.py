import sqlite3
connection=sqlite3.connect('my_database1.db')
cursor=connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students_info(
id INTEGER ,
name TEXT,
age INTEGER,
grade TEXT
)''')800000000
connection.commit()
#connection.close()

cursor.execute('''
INSERT INTO students_info (id,name,age,grade)
VALUES (772003,'Arslan',20,'A')
''')

cursor.execute('''
INSERT INTO students_info (id,name,age,grade)
VALUES (634044,'Tarikh',21,'B')
''')
connection.commit()

cursor.execute('SELECT * FROM students_info')
row=cursor.fetchall()
for row in row:
    print(row)

cursor.execute('''
UPDATE students_info
SET grade ='B'
WHERE name = 'Moon'
''')
connection.commit()