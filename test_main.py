"""
Test goes here

"""

import sqlite3


def test_connection():
    assert sqlite3.connect("cost.db")
