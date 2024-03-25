import sqlite3


def get_cursor(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn.cursor()
