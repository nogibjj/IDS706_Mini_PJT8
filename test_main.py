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
    query = """SELECT y1.username, y1.categories, y1.country,
                AVG(y2.visits), AVG(y2.likes), AVG(y2.comments)
                FROM default.youtubers1DB AS y1
                JOIN default.youtubers2DB AS y2 ON y1.rank = y2.rank
                GROUP BY y1.country
                ORDER BY AVG(y2.visits) DESC
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
