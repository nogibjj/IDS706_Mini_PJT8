import os
import requests
import pandas as pd

def extract(
    url="https://github.com/fivethirtyeight/data/blob/master/hate-crimes/hate_crimes.csv",
    file_path="data/hate_crimes.csv",
    directory="data",
):

    if not os.path.exists(directory):
        os.makedirs(directory)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)

    # Load the CSV into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Split the DataFrame for the following work in the Transform step 
    df1 = df.iloc[:, :6]
    df2 = df.iloc[:, [1,6,7,8,9,10]]

    df1.to_csv(os.path.join(directory, "hate_crimes1.csv"), index=False)
    df2.to_csv(os.path.join(directory, "hate_crimes2.csv"), index=False)

    return file_path
