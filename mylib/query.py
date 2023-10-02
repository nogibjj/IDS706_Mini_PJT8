"""Query the database"""

import sqlite3


def read_data():
    """read data from the databaseery the database for the top 5 rows of the CarsDB table"""
    conn = sqlite3.connect("cost.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM CarsDB LIMIT 10")
    print("Top 10 rows of the CarsDB table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
