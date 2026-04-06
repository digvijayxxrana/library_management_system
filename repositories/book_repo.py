from database.connection import get_connection

class BookRepository:

    def add_book(self,title,author,quantity):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''INSERT INTO books (title,author,quantity) VALUES (?,?,?)''',(title,author,quantity))
        new_book_id = cur.lastrowid
        conn.commit()
        conn.close()
        return new_book_id
    
    def list_all_books(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT * FROM books''')
        books = cur.fetchall()
        conn.close()
        return books
    
    def find_book_by_id(self,id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('''SELECT * FROM books
                    WHERE id = ? ''',(id,))
        return cur.fetchone()
    
    def update_book_quantity(self,id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute('''UPDATE books
                    SET quantity = quantity + 1
                    WHERE id = ?''',(id,))
        conn.commit()
        conn.close()
        
   
    