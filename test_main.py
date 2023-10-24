import pandas as pd

dataset = "murder_2015_final.csv"

def test_mean():
    data = pd.read_csv("murder_2015_final.csv", sep=";")
    assert data['2015_murders'].mean() == 75.48192771