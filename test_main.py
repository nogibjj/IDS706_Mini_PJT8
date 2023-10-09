"""
Tests for the main.py script.
"""

import subprocess


def test_extract():
    """tests extract()"""
    result = subprocess.run(
        ["python", "main.py", "extract"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Extracting data..." in result.stdout


def test_transform_load():
    """tests transform_load()"""
    result = subprocess.run(
        ["python", "main.py", "transform_load"],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    assert "Transforming data..." in result.stdout


def test_general_query():
    """tests general_query()"""
    query = """
    SELECT
        y1.username, y1.categories, y1.country, AVG(y2.visits), AVG(y2.likes), AVG(y2.comments)
    FROM 
        default.youtubers1DB AS y1
    JOIN 
        default.youtubers2DB AS y2
    ON 
        y1.id = y2.id
    GROUP BY  
        y1.categories;
    """
    result = subprocess.run(
        ["python", "main.py", "general_query", query],
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0


if __name__ == "__main__":
    test_extract()
    test_transform_load()
    test_general_query()