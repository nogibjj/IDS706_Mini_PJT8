"""Transform and Load data into the local SQLite3 database"""

import sqlite3
import csv

def load(dataset="youtubers.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("youtubers.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS youtubers")  
    c.execute(
        '''CREATE TABLE youtubers (
            rank INTEGER,
            Username TEXT,
            Categories TEXT,
            Subscribers INTEGER,
            Country TEXT,
            Visits INTEGER,
            Likes INTEGER,
            Comments INTEGER,
            Links TEXT
        )'''
    )   
    c.executemany("INSERT INTO cost VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "youtubers.db "