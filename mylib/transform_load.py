"""Transform and Load data into the local SQLite3 database"""

import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/cost.csv"):
    with open(dataset, "r") as f:
        csv_reader = csv.reader(f, delimiter=",")   
        next(csv_reader, None)  # skip the headers  
        payload = [row for row in csv_reader]

    for row in payload:
        if row[0] == "":    
            print("Empty row detected. Removing from payload.")
    
    conn = sqlite3.connect("cost.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS cost")

    create_table_query = (
           "CREATE TABLE cost ("
            '"date" TEXT,'
            'item TEXT,'
            'cost REAL,'
            'category TEXT,'
            'key TEXT'
            ")"
    )
    c.execute(create_table_query)

    insert_data_query = (
        "INSERT INTO cost (date, item, cost, category, key) VALUES (?, ?, ?, ?, ?)"
    )
    c.executemany(insert_data_query, payload)

    conn.commit()
    conn.close()    
    return "cost.db"    
