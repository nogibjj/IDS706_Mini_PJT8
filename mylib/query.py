"""Query the database"""

import sqlite3


def query(query_statement):
    """Executes passed query and returns the result"""
    conn = sqlite3.connect("cost.db")
    cursor = conn.cursor()
    cursor.execute(query_statement)
    print(cursor.fetchall())
    conn.close()
    return "Success"
