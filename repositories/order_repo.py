from database.connection import get_connection

class OrderRepository:

    def list_latest_orders(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT orders.id,students.name,books.title FROM orders
                    JOIN students ON orders.student_id = students.id
                    JOIN books ON orders.book_id = books.id
                    ORDER BY id DESC''')
        return cur.fetchall()
    
    def find_order_by_id(self,order_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT * FROM orders
                    WHERE id = ?''',(order_id,))
        order= cur.fetchone()
        conn.close()
        return order
    
    
    def create_order(self,student_id,book_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''INSERT INTO orders (student_id,book_id) VALUES (?,?)''',(student_id,book_id))
        latest_order_id = cur.lastrowid
        conn.commit()
        conn.close()
        return latest_order_id
    
    def delete_order(self,student_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''DELETE FROM orders
                    WHERE student_id = ?''',(student_id,))
        count = cur.rowcount
        conn.commit()
        conn.close()
        return count
    
    def find_order_by_student(self,student_id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute('''SELECT * FROM orders 
                    WHERE student_id=?''',(student_id,))
        orders = cur.fetchall()
        conn.close()
        return orders