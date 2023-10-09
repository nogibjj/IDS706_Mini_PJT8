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
        c.execute("SHOW TABLES FROM default LIKE 'youtubers1*'")
        result = c.fetchall()
        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS youtubers1DB (
                    rank int,
                    username string,
                    categories string,
                    subscribers int,
                    country string,
                )
            """
            )

            for _, row in df1.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO youtubers1DB VALUES {convert}")
        c.execute("SHOW TABLES FROM default LIKE 'youtubers2*'")
        result = c.fetchall()

        if not result:
            c.execute(
                """
                CREATE TABLE IF NOT EXISTS youtubers2DB (
                    visits int,
                    likes int,
                    comments int,
                    links string,
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO youtubers2DB VALUES {convert}")
        c.close()

    return "success"
