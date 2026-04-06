from database.connection import get_connection


class StudentRepository:

    def add_student(self, name, age):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name,age) VALUES (?,?)", (name, age))
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_id

    def list_all(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        conn.close()
        return students

    def update_student(self, id, name, age):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE students SET name=?, age=? WHERE id=?", (name, age, id))
        conn.commit()
        conn.close()
        return cursor.rowcount

    def delete_student(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students where id=?", (id,))
        conn.commit()
        conn.close()
        return cursor.rowcount

    def find_student_by_id(self, id):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """SELECT * FROM students
                     WHERE id = ? """,(id,))
        return cur.fetchone()
