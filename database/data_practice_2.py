import sqlite3

def get_connection():
    return sqlite3.connect("library_practice.db")


conn = get_connection()
cursor = conn.cursor()

#cursor.execute('''SELECT id FROM students
#               WHERE name = ?''',("golu",))
#student_id = cursor.fetchone()
#if student_id:
#    student_id = student_id[0]
#else: print("cant find student")

#cursor.execute('''SELECT age FROM students
#               WHERE id = ?''',(student_id,))
#student_age=cursor.fetchone()
#print(student_age)


cursor.execute('''SELECT COUNT(*) FROM students''')
total_students = cursor.fetchone()[0]
print(total_students)


cursor.execute('''SELECT COUNT(*) FROM books
               WHERE quantity > 5''')
result = cursor.fetchone()[0]
print(result)


cursor.execute('''SELECT id FROM students
               WHERE name = ?''',("sukka",))
result = cursor.fetchone()
if result:
    student_id = result[0]
else:print("cant find student")
cursor.execute('''SELECT COUNT(*) FROM orders
               WHERE id = ?''',(student_id,))
print(cursor.fetchone()[0])


cursor.execute('''SELECT SUM(quantity) FROM books''')
total_books = cursor.fetchone()[0]
print(total_books)

#cursor.execute(''' INSERT INTO orders (student_id,book_id) VALUES (?,?)''',(4,1))
#cursor.execute('''UPDATE orders
#               SET order_date = ?
#               WHERE student_id = ?''',("2026-12-12",student_id))
#cursor.execute('''ALTER TABLE orders
#               ADD COLUMN status TEXT DEFAULT 'borrowed' 
#               ''')
#conn.commit()
#cursor.execute('''SELECT * FROM orders
#               ORDER BY id DESC LIMIT 1''')
#latest_id = cursor.fetchone()[0]
#print(latest_id)

cursor.execute('''SELECT name FROM students
               ORDER BY age DESC LIMIT 2''')
old = cursor.fetchall()
cursor.execute('''SELECT id FROM orders
               ORDER BY id DESC LIMIT 1''')
latest_id = cursor.fetchone()[0]
cursor.execute('''UPDATE orders
               SET status = ?
               WHERE id = ?''',("returned",latest_id))
conn.commit()
cursor.execute('''SELECT SUM(quantity) FROM books''')
total_books = cursor.fetchone()[0]
if total_books >20:
    print("large library")
else: print("small library")

cursor.execute('''SELECT students.name,books.title,orders.status FROM orders
               JOIN students ON student_id = students.id
               JOIN books ON book_id = books.id
               WHERE orders.status=?''',("returned",))
order = cursor.fetchall()
print(order)

cursor.execute('''SELECT books.title, COUNT(orders.id) FROM orders
               JOIN books ON orders.book_id = books.id
               GROUP BY books.title''')
print(cursor.fetchall())

cursor.execute('''SELECT students.name,COUNT(orders.id) FROM orders
               JOIN students ON orders.student_id = students.id
               GROUP BY students.name''')
print(cursor.fetchall())

cursor.execute('''SELECT students.name,COUNT(orders.id) FROM orders
               JOIN students ON orders.student_id = students.id
               GROUP BY students.name
               ORDER BY COUNT(orders.id) DESC LIMIT 1''')
print(cursor.fetchall())

# Add more Students
students_data = [
    ('Aman Rana', 22),
    ('Priya Sharma', 19),
    ('Vikram Singh', 25)
]
cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students_data)

# Add more Books
books_data = [
    ('Data Science 101', 5),
    ('SQL Mastery', 3),
    ('Machine Learning', 7),
    ('Digital Marketing', 12)
]
cursor.executemany("INSERT INTO books (title, quantity) VALUES (?, ?)", books_data)

# Add more Orders (Connecting them)
# Note: Check your VS Code Visualizer to make sure these IDs (4, 5, 6 etc) exist!
orders_data = [
    (4, 2, 'Borrowed'), # Aman borrows SQL Mastery
    (5, 1, 'Returned'), # Priya borrows Python Basics
    (5, 3, 'Borrowed'), # Priya borrows Data Science
    (6, 4, 'Borrowed'), # Vikram borrows SQL Mastery
    (4, 5, 'Borrowed')  # Aman borrows Machine Learning
]
cursor.executemany("INSERT INTO orders (student_id, book_id, status) VALUES (?, ?, ?)", orders_data)

conn.commit()
print("Practice data added!")

#print(old)
conn.close()
