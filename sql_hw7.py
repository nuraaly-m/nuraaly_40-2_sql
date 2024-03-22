import sqlite3
db = sqlite3.connect('student')

c = db.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS student(
id INTEGER,
name TEXT,
surname TEXT,
hobby TEXT,
birth_year INTEGER,
hw_points INTEGER)''')

# c.execute('''INSERT INTO student VALUES (1, 'nuraaly', 'melisbekov', 'football', 2005, 11)''')
# c.execute('''INSERT INTO student VALUES (2, 'amir', 'akbashev', 'valleyball', 2006, 10)''')
# c.execute('''INSERT INTO student VALUES (3, 'diyar', 'nadirov', 'wrestling', 2006, 9)''')
# c.execute('''INSERT INTO student VALUES (4, 'denis', 'lukyanov', 'programming', 2006, 8)''')
# c.execute('''INSERT INTO student VALUES (5, 'umar', 'melisbekov', 'basketball', 2009, 7)''')
# c.execute('''INSERT INTO student VALUES (6, 'akbermet', 'myrzataeva', 'sewing', 1982, 6)''')
# c.execute('''INSERT INTO student VALUES (7, 'bekbolot', 'jumagulov', 'programming', 2003, 5)''')
# c.execute('''INSERT INTO student VALUES (8, 'ivan', 'ivanov', 'singing', 1999, 4)''')
# c.execute('''INSERT INTO student VALUES (9, 'masha', 'volkova', 'dancing', 2001, 3)''')
# c.execute('''INSERT INTO student VALUES (10, 'sasha', 'belyi', 'shooting', 1969, 2)''')
# c.execute('''INSERT INTO student VALUES (11, 'student', 'ssstttuuudent', 'ccccc', 1999, 12)''')


c.execute('''SELECT * FROM student WHERE LENGTH(surname) > 10''')
length_surname = c.fetchall()
print("whose surname > 10 symbols: ",length_surname)

c.execute('''UPDATE student SET name = "genius" WHERE hw_points > 10''')

c.execute('''SELECT * FROM student WHERE name = "genius" ''')
genius = c.fetchall()
print("who got more than 10 points: ",genius)

c.execute('''DELETE FROM student WHERE id % 2 = 0''')

c.execute('''SELECT * FROM student''')
students = c.fetchall()
print("all students: ",students)


db.commit()
db.close()
