import sqlite3

def get_connection():
    return sqlite3.connect("library_practice.db")