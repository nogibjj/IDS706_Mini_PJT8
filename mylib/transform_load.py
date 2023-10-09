import os
from databricks import sql
import pandas as pd
from dotenv import load_dotenv


def load(data1="data/youtubers1.csv", data2="data/airline-safety2.csv"):
    df1 = pd.read_csv(data1, delimiter=",", skiprows=1)
    df2 = pd.read_csv(data2, delimiter=",", skiprows=1)
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS TOKEN")
    http_path = os.getenv("HTTP_PATH")
    print(server_h, access_token, http_path)

    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        c = connection.cursor()
        
        c.execute("SHOW TABLES FROM default LIKE 'youtubers1*'")
        result = c.fetchall()

        if len(result) == 0:
            c.execute("CREATE TABLE youtubers1DB (rank INT, name STRING, category STRING, subscribers INT, views INT)")            
            for _, row in df1.iterrows():
                convert = (_,) + tuple(row)
                c.execute(f"INSERT INTO youtubers1DB VALUES {convert}")

        c.execute("SHOW TABLES FROM default LIKE 'youtubers2*'")
        result = c.fetchall()

        if not result:
           c.execute("CREATE TABLE youtubers2DB (visits INT, likes INT, comments INT, links TEXT)")
           for _, row in df2.iterrows():
               convert = tuple(row)
               c.execute(f"INSERT INTO youtubers2DB VALUES {convert}")
           c.close()
                   
    return "success"

if __name__ == "__main__":
    load()