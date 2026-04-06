import sqlite3

def get_connection():
    return sqlite3.connect("library_practice.db")



conn = get_connection()
cur = conn.cursor()

cur.execute('''SELECT students.name,books.title,orders.status FROM orders
            JOIN students ON orders.student_id = students.id
            JOIN books ON orders.book_id = books.id
            WHERE orders.status = ? ''',("Borrowed",))
print(cur.fetchall())

cur.execute('''SELECT students.name,COUNT(orders.id) FROM orders
            JOIN students ON orders.student_id = students.id
            WHERE orders.status = ?
            GROUP BY students.name 
            ORDER BY COUNT(orders.id) DESC''',("Borrowed",))
print(cur.fetchall())

cur.execute('''INSERT INTO books (title,quantity) VALUES (?,?)''',("The Mstery of SQL",1))
conn.commit()

cur.execute('''SELECT students.name,orders.book_id FROM students
            LEFT JOIN orders ON students.id = orders.student_id''')
print(cur.fetchall())