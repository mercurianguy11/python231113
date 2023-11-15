# DemoSqlite3_ex.py
import sqlite3

database_name = './my_database.db'


con = sqlite3.connect(database_name)

cursor = con.cursor()

# SQL = "CREATE TABLE Course (Course_ID int primary key not null, Course_Name text, Course_Date date);"
# cursor.execute(SQL)

# SQL = "SELECT name FROM sqlite_master WHERE type='table';"
# cursor.execute(SQL)
# print(cursor.fetchall())

# SQL = "SELECT sql FROM sqlite_master WHERE type='table';"
# cursor.execute(SQL)
# print(cursor.fetchall())


# SQL = "INSERT INTO Course VALUES(1, 'Algorithm', '2021-03-01');"
# cursor.execute(SQL)
# SQL = "INSERT INTO Course VALUES(2, 'Data Structure', '2021-03-02');"
# cursor.execute(SQL)
# SQL = "INSERT INTO Course VALUES(3, 'Computer Architecture', '2021-03-05');"
# cursor.execute(SQL)
# con.commit()

SQL = "SELECT * FROM Course;"
cursor.execute(SQL)
print(cursor.fetchall())

con.close()

def insert_course(course_id, course_name, course_date):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "INSERT INTO Course VALUES(?, ?, ?);"
    cursor.execute(SQL, (course_id, course_name, course_date))

    con.commit()
    con.close()


def insert_course_list(course_list):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "INSERT INTO Course VALUES(?, ?, ?);"
    cursor.executemany(SQL, course_list)

    con.commit()
    con.close()


def search_course_by_name(course_name):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "SELECT * FROM Course WHERE course_name = ?;"
    cursor.execute(SQL, (course_name, ))

    return cursor.fetchall()


def search_course():
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "SELECT * FROM Course;"
    cursor.execute(SQL)

    return cursor.fetchall()


def search_course_order_by_date(limit):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "SELECT * FROM Course ORDER BY date(course_date) ASC Limit ?;"
    cursor.execute(SQL, (limit, ))

    return cursor.fetchall()


def update_course_by_id(course_id, course_name, course_date):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "UPDATE Course SET course_name = ?, course_date = ? WHERE course_id = ?;"
    cursor.execute(SQL, (course_name, course_date, course_id))

    con.commit()
    con.close()


def delete_course_by_id(course_id):
    con = sqlite3.connect(database_name)
    cursor = con.cursor()

    SQL = "DELETE FROM Course WHERE course_id = ?;"
    cursor.execute(SQL, (course_id, ))

    con.commit()
    con.close()

print(search_course())
delete_course_by_id(1)
delete_course_by_id(2)
delete_course_by_id(3)
print(search_course())
insert_course(1, 'Algorithm', '2021-03-01')
insert_course(2, 'Data Structure', '2021-03-02')
insert_course(3, 'Computer Architecture', '2021-03-05')
course_list = [
    (4, 'Programming Language', '2021-03-04'),
    (5, 'Compiler', '2021-03-01'),
]
print(search_course())
insert_course_list(course_list)
print(search_course_by_name('Algorithm'))
update_course_by_id(1, 'Cyber Security', '2021-03-03')
print(search_course())
print(search_course_order_by_date(100))
print(search_course_order_by_date(100)[::-1])
