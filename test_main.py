"""
Tests for the main.py script.
"""

import subprocess


def test_extract():
    """tests extract()"""
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
    """tests transform_load()"""
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
    """tests general_query()"""
    query = """
    SELECT 
        username, categories, country, AVG(visits), AVG(likes), AVG(comments)
    FROM
        y1 INNER JOIN y2 ON y1.id = y2.id
    GROUP BY
        categories
    ORDER BY 
        visits DESC
    LIMIT 15
    """
    result = subprocess.run(
        [
            "python", 
            "main.py", 
            "general_query", 
            query
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