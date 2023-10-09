"""
Transforms and Loads data into Azure Databricks
"""
import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


def load(dataset1="data/youtubers1.csv", dataset2="data/youtubers2.csv"):
    df1 = pd.read_csv(dataset1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        c.execute("SHOW TABLES FROM default LIKE 'hate_crimes1*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS hate_crimes1DB (
                    state string,
                    median_household_income int,
                    share_unemployed_seasonal float,
                    share_population_in_metro_areas float,
                    share_non_citizen float,
                    share_white_poverty float,
                )
            """
            )

            for _, row in df1.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO hate_crimes1DB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'hate_crimes2*'")
        result = c.fetchall()

        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS hate_crimes2DB (
                    state string,
                    gini_index float,
                    share_non_white float,
                    share_voters_voted_trump float,
                    hate_crimes_per_100k_splc float,
                    avg_hatecrimes_per_100k_fbi float,
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO hate_crimes2DB VALUES {convert}")
        c.close()

    return "success"
