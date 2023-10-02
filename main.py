"""
ETL-Query script
"""

import sys 
from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import query

def main():
    try:
        # Extract
        print("Extracting data...")
        file_path = extract()
        print(f"File extracted to {file_path}")
        
        # Transform and load
        print("Transforming and loading data...")
        load(file_path)
        print("Data loaded into SQLite3 database")

        # Query
        print("Querying data...")
        query()
        print("Query complete")

    except Exception as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    main()  