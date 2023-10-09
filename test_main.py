"""
Tests for the main.py script.
"""

import subprocess


def test_extract():
    result = subprocess.run(
        [
            "python", "main.py", "extract"
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    result = subprocess.run(
        [
            "python", "main.py", "transform_load"
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_general_query():
    result = subprocess.run(
        [
            "python", 
            "main.py", 
            "general_query",
            """SELECT y1.username, y1.categories, y1.country, 
               AVG(y2.visits), AVG(y2.likes), AVG(y2.comments)
               FROM default.youtubers1DB y1
               JOIN default.youtubers2DB y2 ON y1.id = y2.id
               GROUP BY y1.country
               ORDER BY AVG(y2.visits) DESC
               LIMIT 15""", 
        ],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()
    