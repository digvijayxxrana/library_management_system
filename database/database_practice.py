import sqlite3
import os

# --- 1. THE CONNECTION SETTINGS ---
def get_connection():
    # This creates the file in the same folder as this script
    return sqlite3.connect("library_practice.db")

# --- 2. THE RESET COMMAND ---
def reset_database():
    conn = get_connection()
    cur = conn.cursor()
    
    print("Cleaning old tables...")
    cur.execute("DROP TABLE IF EXISTS orders")
    cur.execute("DROP TABLE IF EXISTS students")
    cur.execute("DROP TABLE IF EXISTS books")
    
    print("Creating new tables...")
    cur.execute('''CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
    cur.execute('''CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, quantity INTEGER)''')
    cur.execute('''CREATE TABLE orders (id INTEGER PRIMARY KEY AUTOINCREMENT, student_id INTEGER, book_id INTEGER, order_date TEXT,
                   FOREIGN KEY(student_id) REFERENCES students(id),
                   FOREIGN KEY(book_id) REFERENCES books(id))''')
    
    print("Inserting practice data...")
    students = [("aman", 20), ("rahul", 34), ("golu", 16), ("sukka", 56)]
    books = [("Python Basics", "Author A", 10), ("Advanced SQL", "Author B", 5), ("AI Guide", "Author C", 8)]
    
    cur.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students)
    cur.executemany("INSERT INTO books (title, author, quantity) VALUES (?, ?, ?)", books)
    
    conn.commit()
    conn.close()
    
    # This tells you exactly where to look for the file
    print("\n--- SUCCESS! ---")
    print(f"Database file created at: {os.path.abspath('library_practice.db')}")
    print("Look in your folder for 'library_practice.db'")

# --- 3. THE "GO" BUTTON ---
# This is the part that actually MAKES the file. 
# If you don't have these lines, nothing happens!
if __name__ == "__main__":
    reset_database()