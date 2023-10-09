import subprocess


def test_extract():
    subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
    )


def test_transform_load():
    subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
    )


def test_general_query():
    query = """SELECT a.state, 
               AVG(a.median_household_income), 
               a.share_unemployed_seasonal,
               a.share_population_in_metro_areas,
               b.gini_inex
               FROM default.hate_crimes1DB AS a
               JOIN default.hate_crimes2DB AS b ON a.state = b.state
               ORDER BY b.gini_index 
               LIMIT 10"""
    subprocess.run(
        ["python", "main.py", "general_query", query],
        capture_output=True,
        text=True,
    )


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()
