"""Transform and Load data into the local SQLite3 database"""

import sqlite3
import csv
import os


def load(dataset="data/cost.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("cost.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS cost")  
    c.execute(
        '''CREATE TABLE cost (
            Countries TEXT 
            Cost_of_living,_2017 REAL,
            Global_rank INTEGER,
            Available_data TEXT
        )'''
    )   
    c.executemany("INSERT INTO cost VALUES (?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "cost.db "