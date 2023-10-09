import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv

def load(dataset1="data/hate_crimes1.csv", dataset2="data/hate_crimes2.csv"):
    try:
        load_dotenv()
        server_h = os.getenv("SERVER_HOSTNAME")
        access_token = os.getenv("ACCESS_TOKEN")
        http_path = os.getenv("HTTP_PATH")

        # Check if required environment variables are missing or invalid
        if not server_h or not access_token:
            raise ValueError("Missing or invalid environment variables")
    except Exception as e:
        print("Error loading environment variables:", str(e))
        return "failure"

    try:
        df1 = pd.read_csv(dataset1, delimiter=",")
        df2 = pd.read_csv(dataset2, delimiter=",")
    except Exception as e:
        print("Error reading CSV files:", str(e))
        return "failure"

    try:
        with sql.connect(
            server_hostname=server_h,
            http_path=http_path,
            access_token=access_token,
        ) as connection:
            c = connection.cursor()

            # Check if the tables already exist, handle this case more gracefully
            c.execute("SHOW TABLES FROM default LIKE 'hate_crimes1DB'")
            result1 = c.fetchall()
            c.execute("SHOW TABLES FROM default LIKE 'hate_crimes2DB'")
            result2 = c.fetchall()

            if not result1:
                c.execute(
                    """
                    CREATE TABLE hate_crimes1DB (
                        state string,
                        median_household_income int,
                        share_unemployed_seasonal float,
                        share_population_in_metro_areas float,
                        share_non_citizen float,
                        share_white_poverty float
                    )
                    """
                )

            if not result2:
                c.execute(
                    """
                    CREATE TABLE hate_crimes2DB (
                        state string,
                        gini_index float,
                        share_non_white float,
                        share_voters_voted_trump float,
                        hate_crimes_per_100k_splc float,
                        avg_hatecrimes_per_100k_fbi float
                    )
                    """
                )

            # Insert data into the tables
            for _, row in df1.iterrows():
                convert = tuple(row)
                c.execute("INSERT INTO hate_crimes1DB VALUES (?, ?, ?, ?, ?, ?)", convert)

            for _, row in df2.iterrows():
                convert = tuple(row)
                c.execute("INSERT INTO hate_crimes2DB VALUES (?, ?, ?, ?, ?, ?)", convert)

            c.close()

        return "success"
    except Exception as e:
        print("Error connecting to Databricks or executing SQL:", str(e))
        return "failure"

if __name__ == "__main__":
    result = load()
    print("Load result:", result)
