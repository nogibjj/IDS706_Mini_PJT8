"""Query the database"""

import sqlite3


def query():
    """Read data from the database for the top 10 rows of the 'cost' table."""
    conn = sqlite3.connect("cost.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM cost LIMIT 10"
    )  # Use 'cost' as the table name
    print("Top 10 rows of the 'cost' table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
